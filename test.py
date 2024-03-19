import math
import requests
from bs4 import BeautifulSoup
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription
from lib.crawling.ExchangeRate import ExchangeRate

amazon_url = "https://www.amazon.com/Logitech-Lightspeed-PowerPlay-Compatible-Lightsync/dp/B07L4BM851/ref=sr_1_5?crid=3SFMNLGJRF7E2&dib=eyJ2IjoiMSJ9.BpJCpmeTpx6Awdc9tSfUrnnhVbaquLbx1TEn7JB_Qm6d31W4FXnb55XXCbYs883MOQJA-Jy5IGH1dvnLRh7ljPEkrM1K8l5M9vZnOzLPylXZ9JnOlJYyykAlEMBqHLl49KkgZGLOp9R_VpN8PyxjPlb6wCrB7s-w19LPgAubeNV6sADyhIQQ8HgL3p9_cnybv8M5l8NF6dkaj7bBeahazOXrt3j_c14Nk5RNf5syIRPYBK_cADQezP4JmpbhPv00-ahwJPDKIUSpLqjpNjneS8ADNx7RIgCQ3TVzta9OlBk.iSbiGi87KWODR2dLuM7wFBZ9lpCL1VxR5iWiqqOJAJY&dib_tag=se&keywords=g502&qid=1710834586&s=pc&sprefix=%2Ccomputers%2C616&sr=1-5"

response = requests.get(amazon_url)
soup = BeautifulSoup(response.text, "html.parser")

extractProduct = ExtractProduct(soup)

# print(extractProduct.getTitle()) # 제품명
# print(extractProduct.getImage()) # 제품이미지
# print(extractProduct.getPrice()) # 제품가격
# print(extractProduct.getInfo())  # 제품정보

def escape_unicode(product_info):
    cleaned_product_info = {}
    for key, value in product_info.items():
        cleaned_key = key.replace('\u200e', '')
        cleaned_value = value.replace('\u200e', '')
        cleaned_product_info[cleaned_key] = cleaned_value
    return cleaned_product_info

def calculate_lb(dimensions):
    if weight_unit == "ounces":
        base_price = 10
        if dimensions <= 166:
            return base_price
        else:
            pounds = math.ceil(dimensions / 166)
            additional_cost = (pounds - 1) * 1.5
            return base_price + additional_cost
        
    additional_cost = (dimensions - 1) * 1.5
    return base_price + additional_cost


product_info = escape_unicode(extractProduct.getInfo())
title = extractProduct.getTitle()
price = extractProduct.getPrice()

# 판매이익
profit = round(price * 0.15, 2)

# 국제배송비
weight = product_info['품목 무게'].split()
weight_value = weight[0]
weight_unit = weight[1]

dimensions = eval(product_info['제품 크기'].replace(' ', '').replace('x', '*'))
dimensions = calculate_lb(dimensions)

# 면세 상한가
upper_limit = 200

# 달러 환산가
conversion_price = price

# 환율정보
exchange_rate = float(ExchangeRate())

# 관세
if conversion_price > upper_limit:
    tax = (price + dimensions) * exchange_rate * 0.13
else:
    tax = 0

# 부가세
if conversion_price > upper_limit:
    vat = (price * exchange_rate + dimensions * exchange_rate + tax) * 0.1
else:
    vat = 0

# 스마트스토어 판매가
smart_store_price = int(((price + profit + dimensions) * exchange_rate + tax + vat) / (1-0.05))
print(smart_store_price)
# 네이버수수료
naver_fee = int(smart_store_price * 0.05)
print(naver_fee)



# productDescription = ProductDescription(amazon_url)
# html_code = productDescription.generateHtml()
# print(html_code)
