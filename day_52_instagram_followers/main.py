import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
ACCOUNT = ''
EMAIL = 'uilibrary1'
PASSWORD = 'bigbang@19'

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        self.driver.find_element(By.NAME, 'username').send_keys(EMAIL)
        self.driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

    def find_followers(self):
        self.driver.get('https://www.instagram.com/uiux_designers/')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        pop_up = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for _ in range(5):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',pop_up)
            time.sleep(2)
        time.sleep(3)
    
    def follow(self):
        links = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for link in links:
            if link.text == 'Follow':
                link.click()
                time.sleep(1)
            # try:    
            #     link.click()
            #     time.sleep(2)
            # except Exception:
            #     self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]').click()

insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
