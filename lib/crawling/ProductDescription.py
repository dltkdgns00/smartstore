import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class ProductDescription:
    def __init__(self, amazon_url):
        self.github_image_urls = [
            "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/주의사항.png",
            "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/기간.png",
            "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/통관번호.png",
            "https://raw.githubusercontent.com/dltkdgns00/smartstore/main/images/교환반품.png"
        ]
        self.amazon_url = amazon_url
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
    
    def extractImageUrls(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags = soup.find_all('img')
        image_urls = []
        for img in img_tags:
            src = img.get('src')
            if src and "https://m.media-amazon.com/images/S/aplus-media" in src:
                image_urls.append(src)
        return image_urls

    def generateHtml(self):
        with webdriver.Chrome(options=self.chrome_options) as driver:
            driver.get(self.amazon_url)
            time.sleep(8)
            html_content = driver.page_source

        html_code = "<!DOCTYPE html>\n<html lang=\"ko\">\n<head>\n<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title></title>\n</head>\n<body>\n\n"

        for i, github_url in enumerate(self.github_image_urls, start=1):
            html_code += f"<img src=\"{github_url}\" alt=\"{i} 번째 이미지\">\n\n"

        image_urls = self.extractImageUrls(html_content)

        for i, img_url in enumerate(image_urls, start=len(self.github_image_urls)+1):
            html_code += f"<img src=\"{img_url}\" alt=\"{i} 번째 이미지\">\n\n"

        html_code += "</body>\n</html>"

        return html_code