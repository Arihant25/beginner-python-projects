from selenium import webdriver
from time import time

FIVE_MINUTES = 5 * 60  # Convert 5 minutes to seconds
DRIVER_PATH = "D:\Downloads\chromedriver.exe"


def mk_int(s):
    """Convert to a int, if it can't, return 0"""
    s = s.strip().replace(",", "")
    return int(s) if s else 0


driver = webdriver.Chrome(DRIVER_PATH)

# Open the cookie clicker game
driver.get("http://orteil.dashnet.org/cookieclicker/")

# Find the cookie
cookie = driver.find_element_by_id("bigCookie")

# Set the current time to the start time
oldtime = time()

while True:

    # Find the cookie counter
    cookie_counter = mk_int(driver.find_element_by_xpath(
        '//*[@id="cookies"]').text.split("\n")[0].split(" ")[0])

    # Click on the cookie
    cookie.click()

    # Get the upgrade prices as integers
    cursor_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice0"]').text)
    grandma_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice1"]').text)
    farm_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice2"]').text)
    factory_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice3"]').text)
    mine_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice4"]').text)
    shipment_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice5"]').text)
    alchemy_lab_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice6"]').text)
    portal_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice7"]').text)
    time_machine_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice8"]').text)
    antimatter_condenser_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice9"]').text)
    prism_price = mk_int(driver.find_element_by_xpath(
        '//*[@id="productPrice10"]').text)

    # Check if the cookie score is enough for an upgrade every 5 minutes
    if time() - oldtime > FIVE_MINUTES:

        # Make a list of available upgrades and get the costliest one which can be bought
        available_upgrades = [cursor_price, grandma_price, farm_price, factory_price, mine_price, shipment_price,
                              alchemy_lab_price, portal_price, time_machine_price, antimatter_condenser_price, prism_price]

        available_upgrades = int(max(
            [upgrade for upgrade in available_upgrades if upgrade <= cookie_counter]))

        # Click on that upgrade
        if available_upgrades == 0:
            pass
        elif available_upgrades == cursor_price:
            driver.find_elements_by_class_name('unlocked')[0].click()
        elif available_upgrades == grandma_price:
            driver.find_elements_by_class_name('unlocked')[1].click()
        elif available_upgrades == farm_price:
            driver.find_elements_by_class_name('unlocked')[2].click()
        elif available_upgrades == factory_price:
            driver.find_elements_by_class_name('unlocked')[3].click()
        elif available_upgrades == mine_price:
            driver.find_elements_by_class_name('unlocked')[4].click()
        elif available_upgrades == shipment_price:
            driver.find_elements_by_class_name('unlocked')[5].click()
        elif available_upgrades == alchemy_lab_price:
            driver.find_elements_by_class_name('unlocked')[6].click()
        elif available_upgrades == portal_price:
            driver.find_elements_by_class_name('unlocked')[7].click()
        elif available_upgrades == time_machine_price:
            driver.find_elements_by_class_name('unlocked')[8].click()
        elif available_upgrades == antimatter_condenser_price:
            driver.find_elements_by_class_name('unlocked')[9].click()
        elif available_upgrades == prism_price:
            driver.find_elements_by_class_name('unlocked')[10].click()

        # Set the old time to the current time
        oldtime = time()
