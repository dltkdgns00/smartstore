# 제품명
def extract_product_title(soup):
    product_title = soup.find("title").text
    product_name = product_title.split("Amazon.com: ")[1]
    product_name = product_name.split(" : Electronics")[0]

    return {
        "제품명": product_name
    }