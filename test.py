import requests
from bs4 import BeautifulSoup
from lib.crawling.ExtractProduct import ExtractProduct
from lib.crawling.ProductDescription import ProductDescription

amazon_url = "https://www.amazon.com/Logitech-Lightspeed-PowerPlay-Compatible-Lightsync/dp/B07L4BM851/ref=sr_1_5?crid=3SFMNLGJRF7E2&dib=eyJ2IjoiMSJ9.BpJCpmeTpx6Awdc9tSfUrnnhVbaquLbx1TEn7JB_Qm6d31W4FXnb55XXCbYs883MOQJA-Jy5IGH1dvnLRh7ljPEkrM1K8l5M9vZnOzLPylXZ9JnOlJYyykAlEMBqHLl49KkgZGLOp9R_VpN8PyxjPlb6wCrB7s-w19LPgAubeNV6sADyhIQQ8HgL3p9_cnybv8M5l8NF6dkaj7bBeahazOXrt3j_c14Nk5RNf5syIRPYBK_cADQezP4JmpbhPv00-ahwJPDKIUSpLqjpNjneS8ADNx7RIgCQ3TVzta9OlBk.iSbiGi87KWODR2dLuM7wFBZ9lpCL1VxR5iWiqqOJAJY&dib_tag=se&keywords=g502&qid=1710834586&s=pc&sprefix=%2Ccomputers%2C616&sr=1-5"

response = requests.get(amazon_url)
soup = BeautifulSoup(response.text, "html.parser")

extractProduct = ExtractProduct(soup)

print(extractProduct.getTitle()) # 제품명
print(extractProduct.getImage()) # 제품이미지
print(extractProduct.getPrice()) # 제품가격
print(extractProduct.getInfo())  # 제품정보

# productDescription = ProductDescription(amazon_url)
# html_code = productDescription.generateHtml()
# print(html_code)