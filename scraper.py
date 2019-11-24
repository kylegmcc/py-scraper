import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B07S5QWM6L/ref=sr_1_1_sspa?crid=1C85RKSDFR9CS&keywords=macbook+pro&qid=1574544862&sprefix=macbook%2Caps%2C143&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWU5OOVNSWVNNV0VVJmVuY3J5cHRlZElkPUEwMTY3MjYyT09MTUtENzVSWlk0JmVuY3J5cHRlZEFkSWQ9QTAwNzU4NzM4Sk5SVkFZSEc3NFomd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = {"User-Agent": 'user-agent'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6].replace(',',''))

    send_email()

    print(converted_price)
    print(title.strip())

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender-email-credential', 'sender-email-password-credential')

    subject = 'Price fell down!'
    body = 'The price of this product dropped below the assigned threshold. Check the Amazon link: https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B07S5QWM6L/ref=sr_1_1_sspa?crid=1C85RKSDFR9CS&keywords=macbook+pro&qid=1574544862&sprefix=macbook%2Caps%2C143&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWU5OOVNSWVNNV0VVJmVuY3J5cHRlZElkPUEwMTY3MjYyT09MTUtENzVSWlk0JmVuY3J5cHRlZEFkSWQ9QTAwNzU4NzM4Sk5SVkFZSEc3NFomd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender-email',
        'recipient-email',
        msg
    )
    print('Email has been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)