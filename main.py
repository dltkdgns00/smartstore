from dotenv import load_dotenv
import os
import sys
import requests

from lib.nss.UploadProductImage import ImageUploader
from lib.nss.CreateESign import createESign
from lib.nss.AddProductToNSS import AddProductToNSS
from bs4 import BeautifulSoup
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription


amazon_url = sys.argv[1]

load_dotenv()

# 환경 변수 불러오기
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
telephone_number = os.getenv('TELEPHONE_NUMBER')

# 토큰 요청
eSign_instance = createESign(client_id, client_secret)
bearer_token = eSign_instance.get_token()

# 크롤링
response = requests.get(amazon_url)
soup = BeautifulSoup(response.text, "html.parser")

extractProduct = ExtractProduct(soup)

productTitle = extractProduct.getTitle() # 제품명
image_url = extractProduct.getImage() # 제품이미지
productPrice = extractProduct.getPrice() # 제품가격
productInfo = print(extractProduct.getInfo())  # 제품정보

productDescription = ProductDescription(amazon_url)
html_content = productDescription.generateHtml()

# 이미지 네이버 업로드 후 URL 받아오기
uploader = ImageUploader(bearer_token)

naver_image_url = uploader.return_naver_image_url(image_url)

# 상품 정보 네이버 업로드

# 본문 데이터 변수
leafCategoryId = "" # 카테고리 ID
importer = productInfo['제조사'] # 수입사
sellerBarcode = productInfo['ASIN'] # ASIN
productInfoProvidedNoticeType = "" # 상품정보제공고시 유형

salePrice = 0 # 판매가
# 판매가 계산기 만들것


# 상품 추가
product_instance = AddProductToNSS(telephone_number, bearer_token, productTitle, leafCategoryId, naver_image_url, salePrice, importer, sellerBarcode, productInfoProvidedNoticeType, html_content)
product_instance.add_product()
