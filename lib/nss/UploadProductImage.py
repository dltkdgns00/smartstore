import requests
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')

class ImageUploader:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def return_naver_image_url(self, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)

            url = "https://api.commerce.naver.com/external/v1/product-images/upload"
            headers = {
                'Authorization': "Bearer " + self.bearer_token,
            }

            files = {'imageFiles': ('filename.jpg', image_bytes, 'image/jpeg')}
            response = requests.post(url, headers=headers, files=files)

            return response.text
        else:
            return "이미지 다운로드 실패"