import smtplib
from bs4 import BeautifulSoup
import requests


URL = "https://www.trendyol.com/apple/macbook-pro-16-m2-max-32gb-1tb-ssd-space-gray-laptop-apple-turkiye-garantili-mnwa3tu-a-p-637235161?boutiqueId=621535&merchantId=968"
DESIRED_PRICE = 100000

my_gmail = "your email"
gmail_connection = "smtp.gmail.com"
app_password = "your app pass"
port_number = 587

message_text = 'The Price of Macbook 16" has come under your desired price, it is [PRICE] now.'
subject = f"Great Buying Opportunity!"
msg = f"Subject:{subject}\n\n{message_text}"


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
price_tag = soup.find(name="span", class_="prc-dsc")
price = float(price_tag.text.strip().split()[0].replace(".", "").replace(",", "."))
print(price)

PRICE_EMAIL = msg.replace("[PRICE]", f"{price} TL")

if price < DESIRED_PRICE:
    try:
        with smtplib.SMTP(gmail_connection, port=port_number) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=app_password)
            connection.sendmail(from_addr=my_gmail, to_addrs=my_gmail, msg=PRICE_EMAIL)
        print("The email has been sent.")
    except:
        print("can't send the Email")
