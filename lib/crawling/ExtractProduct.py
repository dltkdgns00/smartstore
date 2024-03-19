
class ExtractProduct:
  def __init__(self, soup):
      self.soup = soup

  # 제품명
  def getTitle(self):
      product_title = self.soup.find("title").text
      product_name = product_title.split("Amazon.com: ")[1]
      product_name = product_name.split(" :")[0]

      return product_name
      
  
  # 제품 가격
  def getPrice(self):
    price_tag = self.soup.find("span", class_="a-offscreen")
    price = price_tag.text.strip()

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

      return {
          "제품 크기": product_dimensions,
          "품목 무게": item_weight,
          "ASIN": asin,
          "품목 모델 번호": item_model_number,
          "제조사": manufacturer
      }
