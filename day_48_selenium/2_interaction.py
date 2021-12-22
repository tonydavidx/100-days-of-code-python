from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(articles_count.text)

driver.quit()
