from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://secure-retreat-92358.herokuapp.com/')

driver.find_element(By.NAME, 'fName').send_keys('Tony')
driver.find_element(By.NAME, 'lName').send_keys('David')
driver.find_element(By.NAME, 'email').send_keys('tony@me.com')
driver.find_element(By.TAG_NAME, 'button').click()
