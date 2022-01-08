import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PROMISSED_SPEED = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.down = 0
        self.wait = WebDriverWait(self.driver, 10)
        self.down_speed = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(By.CLASS_NAME, 'start-text').click()
        time.sleep(80)
        self.down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        return  self.down_speed.text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD)
        except Exception:
            self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys('tonyzillaa')
            self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
            time.sleep(3)
            self.driver.find_element(By.NAME,'password').send_keys(TWITTER_PASSWORD)
            self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block').click()
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys('Hello World')

bot = InternetSpeedTwitterBot()
speed = float(bot.get_internet_speed())
if speed < PROMISSED_SPEED:
    bot.tweet_at_provider()
