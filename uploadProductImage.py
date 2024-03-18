import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

# 이미지 URL
image_url = "https://m.media-amazon.com/images/I/71zPzCm297L._AC_SY879_.jpg"

# 이미지 다운로드
response = requests.get(image_url)
if response.status_code == 200:
    image_bytes = BytesIO(response.content)

    # API 엔드포인트 및 헤더
    url = "https://api.commerce.naver.com/external/v1/product-images/upload"
    headers = {
        'Authorization': "Bearer " + bearer_token,
    }

    # 파일과 함께 POST 요청 보내기
    files = {'imageFiles': ('filename.jpg', image_bytes, 'image/jpeg')}
    response = requests.post(url, headers=headers, files=files)

    # 응답 출력
    print(response.text)
else:
    print("이미지 다운로드 실패")
