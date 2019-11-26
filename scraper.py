import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com.au/Xbox-One-X-1TB-Console/dp/B078D2L6SD/ref=sr_1_1?keywords=xbox&qid=1574754266&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:4]

    if (converted_price <700):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jarrod.dylan.walsh@gmail.com', 'vzqhoahywnwmwquf')

    subject = 'Price has Dropped!'
    body = 'Yayy the price has dropped go to the link now!! https://www.amazon.com.au/Xbox-One-X-1TB-Console/dp/B078D2L6SD/ref=sr_1_1?keywords=xbox&qid=1574754266&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'jarrod.dylan.walsh@gmail.com',
        'livscaglione@gmail.com',
        msg
    )
    print('Hey the Email has been sent!')

    server.quit()


check_price()