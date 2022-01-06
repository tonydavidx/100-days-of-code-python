from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
time.sleep(2)

# locate store items and add them to a list
items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute('id') for item in items]

sec = 5
clicks = 0

timeout = time.time() + 5

while True:
    driver.find_element(By.ID, 'cookie').click()
    if time.time() > timeout:
        all_prices = []
        # get prices of items and add them to list all_prices
        prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        for price in prices:
            if price.text != '':
                cost = price.text.split()[-1].strip().replace(',', '')
                all_prices.append(cost)
# get money by id 
        money = driver.find_element(By.ID, 'money').text
        try:
            money = int(money)
        except ValueError:
            money = int(money.replace(',', ''))
# create a dictionary then write cookie upgrades price as key and item id as value
        cookie_upgrades = {}
        for n in range(len(all_prices)):
            cookie_upgrades[all_prices[n]] = item_ids[n]
        print(f'cookie upgrades: {cookie_upgrades}')
        affordable_upgrades = {}
# iterate through cookie upgrades, check if the money is greater than the price if yes add it to affordable_upgrades dictionary with price and id
        for price, id in cookie_upgrades.items():
            if money > int(price):
                affordable_upgrades[price] = id
        print(f'Affordable upgrades: {affordable_upgrades}')
# get highest affordable item the max function witll return the highest value in the dictionary
        highest_affordable_upgrade = max(affordable_upgrades)
        print(f'Highest affordable upgrade: {highest_affordable_upgrade}')
        to_purchase = affordable_upgrades[highest_affordable_upgrade]
        driver.find_element(By.ID, to_purchase).click()

        timeout = time.time() + 5
