import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "hassaanRaza71@gmail.com"
password = "trix fslf wtlg qwny"


url = "https://a.co/d/11kN3oy"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
price = soup.find(class_="a-offscreen").get_text()
price_in_float = float(price.split("$")[1])

if price_in_float < 297:
    title = soup.find(name="span", id="productTitle").getText().strip()
    subject = f"Price Alert for {title}"
    body = f"{title} is now ${price_in_float}\n{url}"
    
    # Create the email message with UTF-8 encoding
    message = f"Subject: {subject}\n\n{body}".encode('utf-8')
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hassaanraza539@gmail.com",
            msg=message
        )


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
price = soup.find(class_="a-offscreen").get_text()
price_in_float = float(price.split("$")[1])

if price_in_float < 297:
    title = soup.find(name="span", id="productTitle").getText().strip()
    subject = f"Amazon Price Alert!"
    body = f"{title} is now ${price_in_float}\n{url}"
    
    # Create the email message with UTF-8 encoding
    message = f"Subject: {subject}\n\n{body}".encode('utf-8')
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hassaanraza539@gmail.com",
            msg=message
        )
