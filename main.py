import os
import time
import sys
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lib.crawling.Calculator import Calculator
from lib.nss.UploadProductImage import ImageUploader
from lib.nss.CreateESign import createESign
from lib.nss.AddProductToNSS import AddProductToNSS
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def main(amazon_url, productTitle, leafCategoryId):
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
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, "html.parser")

  extractProduct = ExtractProduct(soup)

  # productTitle = extractProduct.getTitle() # 제품명
  image_url = extractProduct.getImage() # 제품이미지
  productPrice = extractProduct.getPrice() # 제품가격
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

  # 국제배송비
  weight = productInfo['품목 무게'].split()
  weight_value = weight[0]
  weight_unit = weight[1]

  calculator = Calculator(
    weight_unit=weight_unit,
    price=productPrice,
    profit=profit
  )

  dimensions = eval(productInfo['제품 크기'].replace(' ', '').replace('x', '*'))
  dimensions = calculator.calculate_lb(dimensions)

  tax, vat = calculator.calculate_taxAndvat(dimensions)

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
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Invalid arguments")