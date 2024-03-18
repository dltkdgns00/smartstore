#!/usr/bin/env python

import requests
import bcrypt
import pybase64
import time
from dotenv import load_dotenv
import os
import urllib.request
import urllib.parse

# .env 파일 로드
load_dotenv()

# 환경 변수 불러오기
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

def get_token(client_id, client_secret, type_="SELF") -> str:
    timestamp = str(int((time.time()-3) * 1000))
    pwd = f'{client_id}_{timestamp}'
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), client_secret.encode('utf-8'))
    client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')

    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_ = {
        "client_id": client_id,
        "timestamp": timestamp,
        "client_secret_sign": client_secret_sign,
        "grant_type": "client_credentials",
        "type": type_
    }

    query = urllib.parse.urlencode(data_)
    url = 'https://api.commerce.naver.com/external/v1/oauth2/token?' + query
    res = requests.post(url=url, headers=headers)
    res_data = res.json()

    while True:
        if 'access_token' in res_data:
            token = res_data['access_token']
            return token
        else:
            print(f'[{res_data}] 토큰 요청 실패')
            time.sleep(1)

token = get_token(client_id=client_id, client_secret=client_secret)
print(f'발급된 토큰 : ', token)
