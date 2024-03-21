import json
from math import ceil
from flask import Flask, jsonify, request, render_template
from dotenv import load_dotenv
import os
import time
from functools import reduce
from operator import mul
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from lib.crawling.Calculator import Calculator
from lib.nss.UploadProductImage import ImageUploader
from lib.nss.CreateESign import createESign
from lib.nss.AddProductToNSS import AddProductToNSS
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def load_category_data(filepath):
    categories = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            category = json.loads(line.strip())
            categories.append(category)
    return categories

app = Flask(__name__)
categories = load_category_data('./디지털,가전 카테고리.csv')  # CSV 파일 경로 지정

@app.route('/search_category')
def search_category():
    query = request.args.get('query', '').lower()
    results = [cat for cat in categories if query in cat['name'].lower() and cat['last'] == "True"]
    return jsonify(results[:5])  # 상위 5개 결과만 반환
    
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

load_dotenv()

smartstoreChannelProductNo = None
amazon_url = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global smartstoreChannelProductNo, amazon_url
    amazon_url = request.form['amazon_url']
    product_title = request.form['product_title']
    product_price = request.form['product_price']
    leafCategoryID = request.form['CategoryID']
    
    # amazon_url 중복방지
    existing_urls = set()
    with open('data.txt', 'r') as f:
        for line in f:
            url = line.split(' : ')[1].strip()
            existing_urls.add(url)

    # 새로 입력된 URL이 이미 존재하는지 확인
    if amazon_url in existing_urls:
        return "이미 등록된 URL입니다."
    
    # 환경 변수 불러오기
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    telephone_number = os.getenv('TELEPHONE_NUMBER')

    # 토큰 요청
    eSign_instance = createESign(client_id, client_secret)
    bearer_token = eSign_instance.get_token()

    # 크롤링
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(amazon_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
    extract_product = ExtractProduct(soup)
    image_url = extract_product.getImage()
    
    product_price = float(product_price)
    
    product_info = extract_product.getInfo()
    
    product_description = ProductDescription(amazon_url)
    html_content = product_description.generateHtml()

    # 이미지 네이버 업로드 후 URL 받아오기
    uploader = ImageUploader(bearer_token)
    naver_image_url = uploader.return_naver_image_url(image_url)

    importer = product_info['제조사']
    seller_barcode = product_info['ASIN']

    profit = round(product_price * 0.15, 2)
    
    item_weight = product_info['품목 무게']
    if item_weight:
        weight = item_weight.split()
        dimensions = int(ceil(float(weight[0])))
        weight_unit = weight[1]
    else:
        dimensions = int(reduce(mul, ExtractProduct.extract_numbers_from_string(product_info['제품 크기'])))
        
    calculator = Calculator(
        weight_unit=weight_unit,
        price=product_price,
        profit=profit
    )
    
    dimensions = calculator.calculate_lb(dimensions)
    print(f"국제배송비는 {dimensions} 입니다.")
    
    tax, vat = calculator.calculate_taxAndvat(dimensions)
    print(f"관세 : {tax}, 부가세 : {vat} 입니다.")
    
    smart_store_price = calculator.calculate_ssp(
        dimensions=dimensions,
        tax=tax,
        vat=vat
    )

    sale_price = smart_store_price

    product_instance = AddProductToNSS(
        telephoneNumber=telephone_number,
        bearer_token=bearer_token,
        name=product_title,
        leafCategoryId=leafCategoryID,
        imageUrl=naver_image_url,
        salePrice=sale_price,
        importer=importer,
        sellerBarcode=seller_barcode,
        html_content=html_content
    )
    smartstoreChannelProductNo = product_instance.add_product()['smartstoreChannelProductNo']

    # 파일에 originProductNo와 amazon_url 저장
    with open('data.txt', 'a') as f:
        f.write(f'{smartstoreChannelProductNo}')
        f.write(' : ')
        f.write(amazon_url)
        f.write('\n')

    return "상품이 성공적으로 추가되었습니다!"

if __name__ == '__main__':
    app.run(debug=True)
