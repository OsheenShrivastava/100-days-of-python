# TODO-1 - Import webdriver,By,Keys and Exceptions from selenium class. Import time.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time

# TODO-2 - Store Login details of Facebook as Global Variables

USERNAME = "Your Email Id"
PASSWORD = "Your Password"

# TODO-3 - Keep chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# TODO-4 - Open the website

driver.get("https://tinder.com/")

time.sleep(5)

I_Accept = driver.find_element(By.XPATH, value='//button[.//div[text()="I accept"]]')
I_Accept.click()

time.sleep(5)

# TODO-5 - Click on Tinder Login Button

Tinder_Login_Button = driver.find_element(By.LINK_TEXT, value="Log in")
Tinder_Login_Button.click()

time.sleep(5)

# TODO-6 - Click on More Options

try:
    More_Options_Button = driver.find_element(By.XPATH, value='//button[contains(text(), "More Options")]')
    More_Options_Button.click()

    time.sleep(1)
    print("Clicked 'More Options' button.")

    # TODO-7 - Click on Login with Facebook Option

    # After clicking "More Options", click "Log in with Facebook" button
    FB_Login_Button = driver.find_element(By.XPATH, value='//button[.//div[text()="Log in with Facebook"]]')
    FB_Login_Button.click()

    print("Clicked 'Log in with Facebook' button after 'More Options'.")

except NoSuchElementException:
    # If "More Options" button not found, try to click "Log in with Facebook" directly
    try:
        FB_Login_Button = driver.find_element(By.XPATH,value='//button[.//div[text()="Log in with Facebook"]]')
        FB_Login_Button.click()

        time.sleep(5)

        print("Clicked 'Log in with Facebook' button directly.")

    except NoSuchElementException:
        print("Neither 'More Options' nor 'Log in with Facebook' buttons found.")


# TODO-8 - Use window handler and switch to facebook window

base_window = driver.window_handles[0]
FB_Login_Window = driver.window_handles[1]
driver.switch_to.window(FB_Login_Window)
print(driver.title)

time.sleep(5)

# TODO-9 - Enter Facebook Login details i.e., Email Id and Password

Email = driver.find_element(By.NAME, value="email")
Email.send_keys("pythontestmail123456789@gmail.com")

Password = driver.find_element(By.NAME, value="pass")
Password.send_keys("Pass@1234")

# TODO-10 - Click on Login Button

try:
    Final_FB_Login_Button = driver.find_element(By.NAME, value="login")
    Final_FB_Login_Button.click()

    print("Clicked Facebook 'Log In' button.")

except (TimeoutException, NoSuchElementException):
    print("Could not find or click the Facebook 'Log In' button.")

# TODO-11 - Click on window which asks to continue as SKOPA and then switch back to tinder window

time.sleep(10)
try:
    Continue_as_Skopa = driver.find_element(By.XPATH, value='//div[@role="button" and .//span[text()="Continue as Skopa"]]')
    Continue_as_Skopa.click()

    print("Clicked 'Continue as Skopa' button.")

except (ElementClickInterceptedException, NoSuchElementException):
    input("Solve CAPTCHA and press Enter...")

    time.sleep(5)

    Continue_as_Skopa = driver.find_element(By.XPATH, value='//div[@role="button" and .//span[text()="Continue as Skopa"]]')
    Continue_as_Skopa.click()

    print("Clicked 'Continue as Skopa' button.")

# TODO-12 - Solve CAPTCHA Manually and press enter

try:
    # TODO-13 - Click on Allow Button and Miss out button

    time.sleep(5)

    driver.switch_to.window(base_window)
    print(driver.title)

    time.sleep(5)

    Allow = driver.find_element(By.XPATH, value='//button[.//div[text()="Allow"]]')
    Allow.click()

    time.sleep(5)

    Miss_out = driver.find_element(By.XPATH, value='//button[.//div[text()="I’ll miss out"]]')
    Miss_out.click()

    time.sleep(5)

except (TimeoutException, NoSuchElementException):
    # TODO-13 - Click on Allow Button and Miss out button

    input("Solve CAPTCHA and press Enter...")

    time.sleep(5)

    driver.switch_to.window(base_window)
    print(driver.title)

    time.sleep(5)

    Allow = driver.find_element(By.XPATH, value='//button[.//div[text()="Allow"]]')
    Allow.click()

    time.sleep(5)

    Miss_out = driver.find_element(By.XPATH, value='//button[.//div[text()="I’ll miss out"]]')
    Miss_out.click()

    time.sleep(5)

# TODO-14 - Hit Like Button with exception Handling
for n in range(100):
    try:
        # Include 1 sec delay between swipes

        # For Dislike Button
        Dislike_Button = driver.find_element(By.XPATH, '//button[.//span[contains(text(), "Nope")]]')
        Dislike_Button.click()

        time.sleep(5)

    except (ElementClickInterceptedException, NoSuchElementException):
        try:
            # input("Solve CAPTCHA and press Enter...")
            time.sleep(10)

            # TODO-15 - Click on Not Interested when Tinder asks to add it on Home Scree

            Not_Interested_Button = driver.find_element(By.XPATH, value='//button[.//div[text()="Not interested"]]')
            Not_Interested_Button.click()

            # wait for 2 secs and then retry
            time.sleep(2)

            # For Dislike Button
            Dislike_Button = driver.find_element(By.XPATH, '//button[.//span[contains(text(), "Nope")]]')
            Dislike_Button.click()

            time.sleep(5)

        except Exception as e:
            print("'Not Interested' button not found or not clickable:", e)

driver.quit()