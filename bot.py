from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from battle import *


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)
browser.implicitly_wait(10)

browser.get('https://play.pokemonshowdown.com')
username = input("Enter username: ")
password = input("Enter password: ")

b_1 = Battle(username, password, browser)

b_1.login()
b_1.begin_battle()

game_over = False

while not game_over: #TODO: fix move choosing
    b_1.choose_move(3)
    try:
        element = WebDriverWait(browser, 150).until(
        EC.presence_of_element_located((By.XPATH, "//button[@value = '3']"))
        )
        browser.find_element(By.NAME, "closeRoom").click()
        time.sleep(1)
    finally:
        browser.quit

time.sleep(200)

