import http.client
from dotenv import load_dotenv
import os
import json

# .env 파일 로드
load_dotenv()

# 환경 변수 불러오기
bearer_token = os.getenv('BEARER_TOKEN')

# print(bearer_token)

conn = http.client.HTTPSConnection("api.commerce.naver.com")

headers = { 'Authorization': 'Bearer ' + bearer_token}

conn.request("GET", "/external/v1/categories?last=false", headers=headers)

res = conn.getresponse()
data = res.read()

# data를 UTF-8로 디코딩하고 JSON으로 파싱
decoded_data = data.decode("utf-8")
json_data = json.loads(decoded_data)

# 'categories' 키가 없고 바로 리스트로 데이터가 제공된다고 가정
# "디지털/가전"이 포함된 카테고리만 필터링하여 출력
if isinstance(json_data, list):  # json_data가 리스트인지 확인
    for category in json_data:
        if "디지털/가전" in category.get('wholeCategoryName', ''):
            print(category)
else:
    print("The response is not a list.")