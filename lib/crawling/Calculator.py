import math

from lib.crawling.ExchangeRate import ExchangeRate

class Calculator:
    def __init__(self, weight_unit, price, profit):
        self.weight_unit = weight_unit
        self.price = price
        self.exchange_rate = float(ExchangeRate())
        self.profit = profit
        self.upper_limit = 200

    def calculate_lb(self, dimensions):
        base_price = 10
        if self.weight_unit == "ounces":
            if dimensions <= 166:
                return base_price
            else:
                pounds = math.ceil(dimensions / 166)
                additional_cost = (pounds - 1) * 1.5
            return base_price + additional_cost
          
        additional_cost = (dimensions - 1) * 1.5
        return base_price + additional_cost

    def calculate_taxAndvat(self, dimensions):
        # 관세
        if self.price > self.upper_limit:
            tax = (self.price + dimensions) * self.exchange_rate * 0.13
        else:
            tax = 0

        # 부가세
        if self.price > self.upper_limit:
            vat = (self.price * self.exchange_rate + dimensions * self.exchange_rate + tax) * 0.1
        else:
            vat = 0

        return [
            tax,
            vat
        ]

   
    def calculate_ssp(self, dimensions, tax, vat):
        # 스마트스토어 판매가
        smart_store_price = int(((self.price + self.profit + dimensions) * self.exchange_rate + tax + vat) / (1-0.05))
        # 반올림하여 1의 자리를 0으로 만들기
        smart_store_price_rounded = round(smart_store_price / 10) * 10
        return smart_store_price_rounded

# # 네이버수수료
# naver_fee = int(smart_store_price * 0.05)
# print(naver_fee)