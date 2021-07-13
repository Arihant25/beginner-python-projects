from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Load Twitter credentials
load_dotenv('.env')
EMAIL = os.getenv('email2')
PASSWORD = os.getenv('email_password_2')
CHROME_DRIVER_PATH = r'D:\Downloads\chromedriver.exe'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        """Get the current internet speed in Mbps"""
        self.driver.get('https://www.speedtest.net/')
        # Click the Go button to start the test
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        # Wait for the test to complete
        sleep(60)
        # Get the download speed
        down_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # Get the upload speed
        up_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        return down_speed, up_speed

    def tweet_internet_speed(self, internet_speed):
        """Tweet the current internet speed"""
        down_speed, up_speed = internet_speed
        # Login to Twitter
        self.driver.get('https://twitter.com/login')
        # Type the email
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(EMAIL)
        # Type the password and submit
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(PASSWORD + Keys.ENTER)
        # Wait for the page to load
        sleep(30)
        # Write the tweet
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(f"Download Speed: {down_speed}Mb/s{Keys.ENTER}Upload speed: {up_speed}Mb/s")
        # Click the Tweet button
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
        # Wait for the tweet to be posted
        sleep(5)
        # Close the window
        self.driver.close()


# Create a new instance of the Twitter bot
bot = InternetSpeedTwitterBot()
# Get the current internet speed and tweet it
bot.tweet_internet_speed(bot.get_internet_speed())
