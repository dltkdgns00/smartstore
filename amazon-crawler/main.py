import requests
from bs4 import BeautifulSoup
from product_information import extract_product_info
from product_title import extract_product_title
from product_price import extract_product_price

url = "https://www.amazon.com/BENFEI-Docking-Silicone-Ethernet-Delivery/dp/B0CTJBSBX7/ref=sr_1_1?crid=1QLAV1Q3CGH18&dib=eyJ2IjoiMSJ9.j98BcHwy-zhN-uGT6IJzY4gOeJDjoak4d8qaK46j3ydDZEyqzKzYRvrIpRgUE-VCx78KTZSucE5yqUVdg9HvEQ.AlYIWD7kBjhJe3HR7YtAcoubmgVursc0P-8PPiquQ0M&dib_tag=se&keywords=BENFEI+USB+C+MST+%ED%97%88%EB%B8%8C&qid=1710811010&sprefix=%2Caps%2C351&sr=8-1"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(extract_product_title(soup)) # 제품명
print(extract_product_price(soup)) # 제품가격
print(extract_product_info(soup))  # 제품정보