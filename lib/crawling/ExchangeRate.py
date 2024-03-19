import requests
from bs4 import BeautifulSoup

def ExchangeRate():
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.find_all('tr'):
        currency_element = row.find('td', class_='tit')
        if currency_element:
            currency = currency_element.text.strip()
            if "미국 USD" in currency:
                exchange_rate_element = row.find_all('td')[4]
                if exchange_rate_element:
                    exchange_rate = exchange_rate_element.text.strip()
                    return float(exchange_rate.replace(',', ''))
    return None
