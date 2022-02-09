import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import links

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(links.zillow)
time.sleep(2)
pagename = driver.title
print(pagename)
# prices = driver.find_elements(By.CLASS_NAME, 'list-card-price').text

# print(prices)

driver.quit()
