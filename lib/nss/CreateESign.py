import requests
import bcrypt
import pybase64
import time
import urllib.parse

class createESign:
    def __init__(self, client_id, client_secret):
        # 클라이언트 ID와 시크릿 직접 설정
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token(self, type_="SELF") -> str:
        timestamp = str(int((time.time()-3) * 1000))
        pwd = f'{self.client_id}_{timestamp}'
        hashed = bcrypt.hashpw(pwd.encode('utf-8'), self.client_secret.encode('utf-8'))
        client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')

        headers = {"content-type": "application/x-www-form-urlencoded"}
        data_ = {
            "client_id": self.client_id,
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
