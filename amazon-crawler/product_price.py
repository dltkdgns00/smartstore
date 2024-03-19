# 제품 가격
def extract_product_price(soup):
    price_tag = soup.find("span", class_="a-offscreen")
    price = price_tag.text.strip()

    return {
        "제품 가격": price
    }