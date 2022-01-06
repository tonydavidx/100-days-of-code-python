import requests
from bs4 import BeautifulSoup
import smtplib
import math
import config

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
product = 'https://www.amazon.in/ASUS-i5-10300H-Graphics-Fortress-FX566LH-HN257T/dp/B08CRMTKMK/'

response = requests.get(product, headers={'User-Agent': user_agent})
soup = BeautifulSoup(response.content, 'lxml')

product_title = soup.find(id='productTitle').get_text().strip()


price = soup.find(
    'span', class_='a-price a-text-price a-size-medium apexPriceToPay')

price = price.getText().split('₹')[1].replace(',', '').split('.')[0]
print(price)


def ten_percent_down(price):
    price = int(price)
    price = price - (price * 0.10)
    price = math.floor(price)
    return price


target_price = ten_percent_down(price)


def send_alert():
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=config.email, password=config.password)
        connection.sendmail(
            from_addr=config.email, to_addrs=config.email, msg=f'Subject: Price Drop alert\n\nProduct: {product_title}\nThe price dropped to {price}')


if int(price) < target_price:
    send_alert()
