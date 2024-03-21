import json
import sys
from math import ceil
from dotenv import load_dotenv
import os
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

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def main(amazon_url, productTitle, productPrice, leafCategoryId):
  load_dotenv()

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

  extractProduct = ExtractProduct(soup)

  # productTitle = extractProduct.getTitle() # 제품명
  image_url = extractProduct.getImage() # 제품이미지
  # productPrice = extractProduct.getPrice() # 제품가격
  productInfo = extractProduct.getInfo()  # 제품정보

  productDescription = ProductDescription(amazon_url)
  html_content = productDescription.generateHtml()

  # 이미지 네이버 업로드 후 URL 받아오기
  uploader = ImageUploader(bearer_token)

  naver_image_url = uploader.return_naver_image_url(image_url)

  # 본문 데이터 변수
  # leafCategoryId = "50000003" # 카테고리 ID
  importer = productInfo['제조사'] # 수입사
  sellerBarcode = productInfo['ASIN'] # ASIN

  # 판매이익
  profit = round(productPrice * 0.15, 2)
    
  item_weight = productInfo['품목 무게']
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



  # 스마트스토어 판매가
  smart_store_price = calculator.calculate_ssp(
    dimensions=dimensions,
    tax=tax,
    vat=vat
  )

  salePrice = smart_store_price

  # 상품 추가
  product_instance = AddProductToNSS(
    telephoneNumber=telephone_number,
    bearer_token= bearer_token,
    name=productTitle,
    leafCategoryId=leafCategoryId,
    imageUrl=naver_image_url,
    salePrice=salePrice,
    importer=importer,
    sellerBarcode=sellerBarcode,
    html_content=html_content
  )
  smartstoreChannelProductNo =  product_instance.add_product()['smartstoreChannelProductNo']

  # 파일에 originProductNo와 amazon_url 저장
  with open('아마존url저장.txt', 'a') as f:
    f.write(f'{smartstoreChannelProductNo}')
    f.write(' : ')
    f.write(amazon_url)
    f.write('\n')

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Invalid arguments")