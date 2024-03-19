from dotenv import load_dotenv
import os

from lib.nss.UploadProductImage import ImageUploader
from lib.nss.CreateESign import createESign
from lib.nss.AddProductToNSS import AddProductToNSS

load_dotenv()

# 환경 변수 불러오기
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
telephone_number = os.getenv('TELEPHONE_NUMBER')

# 토큰 요청
eSign_instance = createESign(client_id, client_secret)
bearer_token = eSign_instance.get_token()

# 크롤링

# 이미지 네이버 업로드 후 URL 받아오기
image_url = "" # 이미지 URL

uploader = ImageUploader(bearer_token)

naver_image_url = uploader.return_naver_image_url(image_url)

# 상품 정보 네이버 업로드

# 본문 데이터 변수
name = "" # 상품명
leafCategoryId = "" # 카테고리 ID
imageUrl = "" # 상품 이미지 URL
salePrice = 0 # 판매가
importer = "" # 수입사
sellerBarcode = "" # ASIN
productInfoProvidedNoticeType = "" # 상품정보제공고시 유형

# HTML 콘텐츠
html_content = """"""

# 상품 추가
product_instance = AddProductToNSS(telephone_number, bearer_token, name, leafCategoryId, imageUrl, salePrice, importer, sellerBarcode, productInfoProvidedNoticeType, html_content)
product_instance.add_product()
