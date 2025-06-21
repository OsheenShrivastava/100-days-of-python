
# TODO-1 - Import requests and Beautiful Soup

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"

# TODO-2 - Add Header

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0."
                  "4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# TODO-3 - Open the link, pass header and get data

response = requests.get(url=URL, headers=header)
response.raise_for_status()
webpage = response.text

# TODO-4 - Create an Object of Beautiful Soup and parse html file

soup = BeautifulSoup(webpage, "html.parser")

# TODO-5 - Create a list of all links

anchor_tags = soup.select(".StyledPropertyCardDataWrapper a")
link_list = []

for tag in anchor_tags:
    link_list.append(tag.get("href"))

# TODO-6 - Create a list of all the prices

prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")
price_list = []

for price in prices:
    price_list.append(price.text.strip("+/mo").strip("+ 1bd"))

# TODO-7 - Create a list of all the addresses

addresses = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
address_list = []

for address in addresses:
    address_list.append(address.text.replace("|","").replace("\n","").strip())

# TODO-8 - Import Selenium and Open google chrome

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# TODO-9 - Import time and Open the google form link

Google_Form_Link = "Your Google Form Link"

driver.get(Google_Form_Link)

time.sleep(5)

# TODO-10 - Create text input links for Address,Price and Link

Address_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
Price_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
Link_path = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

# TODO-11 - Create FOR loop to run for number of items present in lists

for item in range(len(link_list)):
    # TODO-12 - Fill the google form with price,link and address for all items

    Address = driver.find_element(By.XPATH, value=Address_path)
    Address.send_keys(address_list[item], Keys.ENTER)

    time.sleep(1)

    Price = driver.find_element(By.XPATH, value=Price_path)
    Price.send_keys(price_list[item], Keys.ENTER)

    time.sleep(1)

    Link = driver.find_element(By.XPATH, value=Link_path)
    Link.send_keys(link_list[item], Keys.ENTER)

    time.sleep(1)

    # TODO-13 - Click on Submit button.

    Submit_Button = driver.find_element(By.CSS_SELECTOR, value='div[role="button"][aria-label="Submit"]')
    Submit_Button.click()

    time.sleep(1)

    # TODO-14 - Click on Submit another response button.

    Submit_another_response_link = driver.find_element(By.CSS_SELECTOR, value='.c2gzEf a')
    Submit_another_response_link.click()

    time.sleep(1)