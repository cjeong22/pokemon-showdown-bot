from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

import time

class Battle:
    def __init__(self, username, password, browser):
        self.username = username
        self.password = password
        self.browser = browser


    def login(self):
        self.browser.find_element(By.NAME, "login").click()
        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//button[@type = 'submit']").click()
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.XPATH, "//button[@type = 'submit']").click()

    def begin_battle(self):
        time.sleep(1)
        self.browser.find_element(By.NAME, "search").click()

    def choose_move(self, move_num : int):
        if move_num == 1:
            self.browser.find_element(By.XPATH, "//button[@value = '1']").click()
        elif move_num == 2:
            self.browser.find_element(By.XPATH, "//button[@value = '2']").click()
        elif move_num == 3:
            self.browser.find_element(By.XPATH, "//button[@value = '3']").click()
        else:
            self.browser.find_element(By.XPATH, "//button[@value = '4']").click()

    def game_over(self):
        self.browser.find_element(By.NAME, "closeRoom").click()
        time.sleep(1)
        try:
             self.browser.find_element(By.XPATH, "//button[@type = 'submit']")
             return False
        except NoSuchElementException:
             self.browser.find_element(By.NAME, "close").click()
             return True


    

