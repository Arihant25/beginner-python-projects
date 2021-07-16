import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = r"D:\Downloads\chromedriver.exe"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# URL to the websites
zillow_url = "https://bit.ly/3xJ3ZFJ"
form_url = "https://forms.gle/uS42zqLeiFF9mh8p9"
# Get the website content using requests
response = requests.get(zillow_url, headers=HEADERS)
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


def get_zillow_data():
    """Get the housing data from Zillow"""
    soup = BeautifulSoup(response.text, "html.parser")
    # Get the address of each house
    address_list = [address.get_text().split(" | ")[-1]
                    for address in soup.find_all("address")]
    # Get the price of each house
    price_list = [price.get_text().split("+")[0]
                  for price in soup.select("div .list-card-price")]
    # Get the link to each house
    link_list = [link.get("href")
                 for link in soup.select("li a.list-card-link")]
    for link in soup.select("li a.list-card-link"):
        if "http" in link.get_text():
            link_list.append(link.get_text())
        else:
            link_list.append("https://www.zillow.com" + link.get_text())

    return address_list, price_list, link_list


def fill_google_form(housing_data):
    """Enter the housing data in the Google Form"""
    for i in range(len(housing_data[0])):
        driver.get(form_url)
        sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(housing_data[0][i] + Keys.TAB + housing_data[1][i] + Keys.TAB + housing_data[2][i] + Keys.TAB + Keys.ENTER)


fill_google_form(get_zillow_data())
