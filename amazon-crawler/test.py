import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def extract_image_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    image_urls = []
    for img in img_tags:
        src = img.get('src')
        if src and "https://m.media-amazon.com/images/S/aplus-media-library-service-media" in src:
            image_urls.append(src)
    return image_urls

def generate_html_code(github_image_urls, amazon_url):
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get(amazon_url)
        time.sleep(8)

        html_content = driver.page_source

    html_code = "<!DOCTYPE html>\n<html lang=\"ko\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title></title>\n</head>\n<body>\n\n"

    for i, github_url in enumerate(github_image_urls, start=1):
        html_code += f"<img src=\"{github_url}\" alt=\"{i} 번째 이미지\">\n\n"

    image_urls = extract_image_urls(html_content)

    for i, img_url in enumerate(image_urls, start=len(github_image_urls)+1):
        html_code += f"<img src=\"{img_url}\" alt=\"{i} 번째 이미지\">\n\n"

    html_code += "</body>\n</html>"

    return html_code

github_image_urls = [
    "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/주의사항.png",
    "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/기간.png",
    "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/통관번호.png",
    "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/교환반품.png"
]

amazon_url = "https://www.amazon.com/Anker-Charging-MacBook-Galaxy-Charger/dp/B088NRLMPV?ref_=Oct_d_oup_d_172456_0&pd_rd_w=h2XTq&content-id=amzn1.sym.f3b85eb4-28cc-44b6-8305-47829ac57b78&pf_rd_p=f3b85eb4-28cc-44b6-8305-47829ac57b78&pf_rd_r=QF8M41192712PEKSVFMK&pd_rd_wg=LtFAw&pd_rd_r=a002a34c-8d32-4726-9b21-e9e8be8d70ed&pd_rd_i=B088NRLMPV&th=1"#"https://www.amazon.com/BENFEI-Docking-Silicone-Ethernet-Delivery/dp/B0CTJBSBX7/ref=sr_1_1?crid=1QLAV1Q3CGH18&dib=eyJ2IjoiMSJ9.j98BcHwy-zhN-uGT6IJzY4gOeJDjoak4d8qaK46j3ydDZEyqzKzYRvrIpRgUE-VCx78KTZSucE5yqUVdg9HvEQ.AlYIWD7kBjhJe3HR7YtAcoubmgVursc0P-8PPiquQ0M&dib_tag=se&keywords=BENFEI+USB+C+MST+%ED%97%88%EB%B8%8C&qid=1710811010&sprefix=%2Caps%2C351&sr=8-1"

html_code = generate_html_code(github_image_urls, amazon_url)
print(html_code)
