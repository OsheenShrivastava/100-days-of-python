# TODO-1 - Import BeautifulSoup from bs4 module and requests module

from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv

# TODO-2 - Get the response for Live URL and save its text to a variable called webpage

# Static URL
# URL = "https://appbrewery.github.io/instant_pot/"

# Live URL
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# TODO-9 - Add some headers to your request in the main.py. At minimum add the User-Agent and Accept-Language.
#  At most copy the full header from https://httpbin.org/headers (excluding the host and X-Amzn-Trace-id)

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 "
                  "Safari/537.36",
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()
webpage = response.text

# TODO-3 - Use BeautifulSoup module to parse data to html.
soup = BeautifulSoup(webpage, 'html.parser')

# TODO-4 - Get hold of the price of the item as a floating point number and print it out.

# For Static URL
# price = float(soup.find(class_="aok-offscreen").text.split("$")[1])

# For Live URL
price = float(soup.find(class_="aok-offscreen").text.split("$")[1].split()[0])

print(price)

# TODO-5 - Get hold of title of product, split it to store it in the form of a list and join them using " "
#  (single space)
title = ' '.join(soup.find(id="productTitle").getText().split())
# print(title)

# TODO-6 - Set a target price
target_price = 100.0

# TODO-7 - Create a .env file. Import os and dotenv at the top and export all the credentials from .env to main.py file
# Load the .env file
load_dotenv()

# Access the environment variables
SMTP_Address = os.environ["SMTP_ADDRESS"]
Email_Address = os.environ["EMAIL_ADDRESS"]
Email_Password = os.environ["EMAIL_PASSWORD"]

message = ""
# TODO-8 - Check if current price is less than target price. If yes then send an email
if price < target_price:
    message = str(title) + " is now $" + str(price) + " " + "\n" + str(URL)
    print(message)

    with SMTP(SMTP_Address, port=587) as connection:
        connection.starttls()
        connection.login(user=Email_Address, password=Email_Password)
        connection.sendmail(
            from_addr=Email_Address,
            to_addrs=Email_Address,
            msg=f"Subject: Amazon Price Alert!\n\n{message}".encode("utf-8")
        )