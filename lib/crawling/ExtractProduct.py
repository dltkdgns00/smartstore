class ExtractProduct:
  def __init__(self, soup):
      self.soup = soup

  @staticmethod
  def escapeUnicode(product_info):
    cleaned_product_info = {}
    for key, value in product_info.items():
        cleaned_key = key.replace('\u200e', '')
        cleaned_value = value.replace('\u200e', '')
        cleaned_product_info[cleaned_key] = cleaned_value
    return cleaned_product_info

  # 제품명
  def getTitle(self):
    product_title = self.soup.find("title").text
    print(product_title)
    product_name = product_title.split(": ")[1]

    return product_name
  
  # 제품 가격
  def getPrice(self):
    price_tag = self.soup.find("span", class_="a-price-whole")
    price = price_tag.text.strip()
    price = float(price.replace("$", ""))
    
    return price
  
  # 제품 사진
  def getImage(self):
    image_tag = self.soup.find("img", id="landingImage")
    image_url = image_tag["src"]

    return image_url
  
  # 제품 정보
  def getInfo(self):
      product_info_tags = self.soup.find_all("tr")

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

      product_info = {
          "제품 크기": product_dimensions,
          "품목 무게": item_weight,
          "ASIN": asin,
          "품목 모델 번호": item_model_number,
          "제조사": manufacturer
      }

      product_info = self.escapeUnicode(product_info)

      return product_info