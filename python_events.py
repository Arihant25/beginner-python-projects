from selenium import webdriver
from pprint import pprint

DRIVER_PATH = "D:\Downloads\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(DRIVER_PATH)

# Open the website
driver.get("https://www.python.org")

# Get the list of events
list = driver.find_element_by_xpath(
    '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

list_items = list.find_elements_by_tag_name("li")

result = {}

# Get the event information for each event
for i in range(len(list_items)):
    event = list_items[i]
    name = event.text.split('\n')[1]
    date = event.find_element_by_tag_name(
        "time").get_attribute("datetime").split('T')[0]
    result[i] = {'name': name, 'date': date}

# Quit the window
driver.quit()

# Print the dictionary
pprint(result)
