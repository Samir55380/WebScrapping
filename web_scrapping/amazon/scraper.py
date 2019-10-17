import requests
from email_manager import send_email
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter

c = CurrencyConverter()
URL = 'https://www.amazon.com/Yeelight-Dimmable-Changing-Equivalent-Compatible/dp/B077GCYCT7/ref=nav_signin?crid' \
      '=2CHRQZC7E10IJ&keywords=yeelight&qid=1571256850&sprefix=yee%2Caps%2C241&sr=8-5& '

session = requests.Session()

session.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-PT,pt;q=0.8,en;q=0.5,en-US;q=0.3',
    'Referer': 'Referer: https://www.amazon.com/ap/signin'
}

resp = session.get(URL)
html = resp.text

soup = BeautifulSoup(html, 'lxml')

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text()

price_final = price.replace('$', '')

convert_curr = c.convert(float(price_final), 'USD', 'EUR')
final_converted_price = ("%.2f" % convert_curr)

if float(final_converted_price) < float(17.00):
    send_email()

print("Product {} is valued now {} Euro".format(title, final_converted_price))
send_email()
