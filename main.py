from dotenv import load_dotenv
import os
import sys
import requests

from lib.crawling.Calculator import Calculator
from lib.nss.UploadProductImage import ImageUploader
from lib.nss.CreateESign import createESign
from lib.nss.AddProductToNSS import AddProductToNSS
from bs4 import BeautifulSoup
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription


# amazon_url = sys.argv[1]
amazon_url = "https://www.amazon.com/Elgato-Stream-Deck-MK-2-Controller/dp/B09738CV2G?ref_=Oct_d_omwf_d_172456_4&pd_rd_w=Pbx0C&content-id=amzn1.sym.e1dd8637-4da2-4f16-81ea-1bd7ea3eed24&pf_rd_p=e1dd8637-4da2-4f16-81ea-1bd7ea3eed24&pf_rd_r=FK71VJX8X1YFJAFQZ8BQ&pd_rd_wg=GTBfu&pd_rd_r=b3e2a08e-8c62-4d1f-8eb3-c3a0214f1d74&pd_rd_i=B09738CV2G&th=1"

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
if response.status_code != 200:
  print(response.text)
  print("Amazon URL이 올바르지 않습니다.")
  sys.exit()
soup = BeautifulSoup(response.text, "html.parser")

extractProduct = ExtractProduct(soup)

productTitle = extractProduct.getTitle() # 제품명
image_url = extractProduct.getImage() # 제품이미지
productPrice = extractProduct.getPrice() # 제품가격
productInfo = extractProduct.getInfo()  # 제품정보

productDescription = ProductDescription(amazon_url)
html_content = productDescription.generateHtml()

# 이미지 네이버 업로드 후 URL 받아오기
uploader = ImageUploader(bearer_token)

naver_image_url = uploader.return_naver_image_url(image_url)

# 본문 데이터 변수
leafCategoryId = "50000003" # 카테고리 ID
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
product_instance.add_product()
