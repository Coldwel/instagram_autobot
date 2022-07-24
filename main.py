from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

CHROME_DRIVER_PATH = "location of chrome driver on your computer"
SIMILAR_ACCOUNT = "https://www.instagram.com/marvel/"
USERNAME = "Your username"
PASSWORD = "Your password"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        login_username = self.driver.find_element(By.NAME, "username")
        login_username.send_keys(USERNAME)
        login_password = self.driver.find_element(By.NAME, "password")
        login_password.send_keys(PASSWORD)
        time.sleep(2)
        login_password.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.get(SIMILAR_ACCOUNT)

    def find_followers(self):
        time.sleep(3)
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers.click()
        time.sleep(1)

    def follow(self):
        time.sleep(2)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for buttons in all_buttons:
            if buttons.text == "Follow":
                self.driver.implicitly_wait(10)
                time.sleep(random.randint(1000, 1600) / 1000)
                buttons.click()
            elif buttons.text != "Follow":
                cancel_button = self.driver.find_elements(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
