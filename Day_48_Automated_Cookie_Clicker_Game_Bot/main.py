
# TODO-1 - Import webdriver,By and Keys from selenium class

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# TODO-2 - Keep chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# TODO-3 - Open the website

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# TODO-4 - Get the cookie
click_the_cookie = driver.find_element(By.ID, value="cookie")

# TODO-5 - Import time module at the top and check affordable upgrades evey 5 secs

# Ideal timeout is 5 secs
Timeout = 5
Current_time = time.time()
Minutes_5 = time.time() + 60*5

while time.time() <= Minutes_5:
    Delta = time.time() - Current_time

    click_the_cookie.click()

    if Delta >= Timeout:

        # TODO-6 - Get the value for Money in account
        Money = driver.find_element(By.ID, value="money").text
        if "," in Money:
            Money = Money.replace(",", "")

        Cookie_count = int(Money)


        # TODO-7 - Get all the upgrades and their cost
        Store_elements = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        Store_dict = {}
        for element in Store_elements:
            full_text = element.text.strip()

            if ' - ' in full_text:
                name_part, price_part = full_text.split(' - ')
                Store_dict[name_part] = price_part

        # print(Store_dict)

        #  TODO-8 - Create a list of affordable items.

        Affordable_items_dict = {}

        for key,value in Store_dict.items():
            if "," in value:
                value = value.replace(",", "")

            if Cookie_count > int(value):
                Affordable_items_dict[key] = int(value)

        print(f"Affordable items: {Affordable_items_dict}")

        # TODO-9 - Check upgrades price and find the most expensive one.

        Most_Expensive_Upgrade_value = 0
        Most_Expensive_Upgrade_name = ""

        for key,value in Affordable_items_dict.items():
            if Most_Expensive_Upgrade_value < value:
                Most_Expensive_Upgrade_value = value
                Most_Expensive_Upgrade_name = str(key)

        print(f"Most expensive upgrade: {Most_Expensive_Upgrade_value}")
        print("5 secs over")

        # TODO-10 - Create an element_ID since clicking requires to ID name to click.
        #  Click on the most expensive items to purchase.


        if Most_Expensive_Upgrade_name:
            element_ID = f"buy{Most_Expensive_Upgrade_name}"

            Purchase = driver.find_element(By.ID, value=element_ID)
            Purchase.click()

        Current_time = time.time()

    # TODO-11 - Print Cookies per sec from the site every 5 minutes

    if time.time() > Minutes_5:
        Cookies_Per_Sec = driver.find_element(By.ID, value="cps").text
        print(f"cookies/second: {Cookies_Per_Sec}")

        Minutes_5 = time.time() + 60*5