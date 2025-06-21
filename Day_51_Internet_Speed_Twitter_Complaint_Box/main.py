
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# TODO-1 - Add these constants in the file
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "Your Twitter Email"
TWITTER_PASSWORD = "Your Twitter Password"
TWITTER_USERNAME = "Your Twitter Username"


# TODO-2 - Create a class called InternetSpeedTwitterBot


class InternetSpeedTwitterBot:
    def __init__(self):
        # TODO-3 - In the init() method, import and create the Selenium
        #  driver. Keep chrome browser open after program finishes.

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)

        # TODO-4 - Initialize down and up properties in init() method
        self.up = 0
        self.down = 0

    # TODO-5 - Create two methods - get_internet_speed() and tweet_at_provider(). Import By, Keys and Exceptions

    def get_internet_speed(self):
        # TODO-6 - Open the website
        self.driver.get("https://www.speedtest.net/")

        time.sleep(5)

        # TODO-7 - Click on Continue button
        Continue_button = self.driver.find_element(By.ID, value='onetrust-accept-btn-handler')
        Continue_button.click()

        # TODO-8 - Click on Go button
        Go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        Go_button.click()

        # TODO-9 - Import time and Wait for 50 secs to load internet speed
        time.sleep(40)

        # TODO-10 - Extract upload and download speed
        self.down = self.driver.find_element(By.CSS_SELECTOR, value= '.result-data-large.result-data-value.download-speed').text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value='.result-data-large.result-data-value.upload-speed').text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        # TODO-11 - Login to Twitter Account
        self.driver.get("https://x.com/i/flow/login")

        # TODO-12 - Wait for 10 secs
        time.sleep(10)

        # TODO-13 - Enter Username and Click on Next
        Email = self.driver.find_element(By.NAME, value="text")
        Email.send_keys(TWITTER_EMAIL, Keys.ENTER)

        time.sleep(3)

        try:
            # TODO-14 - Enter Password and Click on Login
            Password = self.driver.find_element(By.NAME, value="password")
            Password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            time.sleep(10)

        # TODO-15 - Add exception if username appears instead of password
        except NoSuchElementException:
            Enter_Username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            Enter_Username.send_keys(TWITTER_USERNAME, Keys.ENTER)

            time.sleep(3)

            Password = self.driver.find_element(By.NAME, value="password")
            Password.send_keys(TWITTER_PASSWORD, Keys.ENTER)

            time.sleep(10)

        # TODO-16 - Click on New Tweet Button
        New_Tweet_Button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        New_Tweet_Button.click()

        # TODO-17 - Wait for it to load
        time.sleep(15)

        # TODO-18 - Enter new tweet
        Enter_tweet = self.driver.find_element(By.CSS_SELECTOR, value='div[role="textbox"]')
        Tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        Enter_tweet.send_keys(Tweet)

        # TODO-19 - Click on Post button
        Post_Button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="tweetButton"]')
        Post_Button.click()

        time.sleep(2)
        # self.driver.quit()

Twitter_Bot = InternetSpeedTwitterBot()

Twitter_Bot.get_internet_speed()

Twitter_Bot.tweet_at_provider()