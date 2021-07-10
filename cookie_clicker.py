from selenium import webdriver

DRIVER_PATH = "D:\Downloads\chromedriver.exe"
driver = webdriver.Chrome(DRIVER_PATH)

# Open the cookie clicker game
driver.get("http://orteil.dashnet.org/cookieclicker/")

# Find the cookie
cookie = driver.find_element_by_id("bigCookie")

counter = 0

while True:

    counter += 1

    # Click on the cookie
    cookie.click()

    # Click on the upgrades
    if counter % 100 == 0:
        for i in range(8, 0, -1):
            try:
                driver.find_element_by_xpath(
                    f'/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div[{i}]').click()
            except:
                pass
