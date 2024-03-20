import re

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
  
  @staticmethod
  def remove_control_characters(text):
      return re.sub(r'[\u200b-\u200f\u202a-\u202e\u2060-\u2064]+', '', text)
    
  @staticmethod
  def clean_dict(self, dictionary):
    cleaned_data = {}
    for key, value in dictionary.items():
        cleaned_key = self.remove_control_characters(key).strip()
        cleaned_value = self.remove_control_characters(value).strip()
        cleaned_data[cleaned_key] = cleaned_value
    return cleaned_data
  
  # 제품명
  def getTitle(self):
    product_title = self.soup.find("title").text
    print(product_title)
    product_name = product_title.split(": ")[1]

    return product_name
  
  # 제품 가격
  def getPrice(self):
    price_tag = self.soup.find("span", class_="a-price-whole")
    price = int(price_tag.text.strip().replace('.', ''))+1
    
    return price
  
  # 제품 사진
  def getImage(self):
    image_tag = self.soup.find("img", id="landingImage")
    image_url = image_tag["src"]

    return image_url
  
  # 제품 정보
  def getInfo(self):
      extracted_data = {}

      # CSS 선택자를 사용하여 데이터 추출
      items = self.soup.select('#detailBullets_feature_div .a-list-item')
      if items:
        # 각 항목에서 텍스트 추출하여 딕셔너리에 추가
        for item in items:
            text = item.get_text(strip=True)
            key = text.split(':')[0].strip()
            value = text.split(':')[-1].strip()
            extracted_data[key] = value
            
        extracted_data = self.clean_dict(self, {self.remove_control_characters(key): self.remove_control_characters(value) for key, value in extracted_data.items()})
        
        product_dimensions = extracted_data.get("Package Dimensions", "").split(";")[0].strip().replace(" inches", "")
        item_weight = extracted_data.get("Package Dimensions", "").split(";")[1].strip() if len(extracted_data.get("Package Dimensions", "").split(";")) > 1 else None
        asin = extracted_data.get("ASIN", None)
        item_model_number = extracted_data.get("Item model number", None)
        manufacturer = extracted_data.get("Manufacturer", None)

        # 결과 출력
        print("Product Dimensions:", product_dimensions)
        print("Item Weight:", item_weight)
        print("ASIN:", asin)
        print("Item model number:", item_model_number)
        print("Manufacturer:", manufacturer)
      else:
        
      #- ------------------
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
                if key == "Product Dimensions" or key == "Package Dimensions":
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