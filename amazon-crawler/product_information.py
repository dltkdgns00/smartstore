# 제품 정보
def extract_product_info(soup):
    product_info_tags = soup.find_all("tr")

    product_dimensions = ""
    item_weight = ""
    asin = ""
    item_model_number = ""
    manufacturer = ""

    for tag in product_info_tags:
        th = tag.find("th", class_="a-color-secondary a-size-base prodDetSectionEntry")
        td = tag.find("td", class_="a-size-base prodDetAttrValue")
        if th and td:
            key = th.text.strip()
            value = td.text.strip()
            if key == "Product Dimensions":
                value = value.replace(" inches", "")
                product_dimensions = value
            elif key == "Item Weight":
                item_weight = value
            elif key == "ASIN":
                asin = value
            elif key == "Item model number":
                item_model_number = value
            elif key == "Manufacturer":
                manufacturer = value

    return {
        "제품 크기": product_dimensions,
        "품목 무게": item_weight,
        "ASIN": asin,
        "품목 모델 번호": item_model_number,
        "제조사": manufacturer
    }
