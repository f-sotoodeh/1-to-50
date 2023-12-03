from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


URL = 'https://zzzscore.com/1to50/en/'
BOX = '//div[@style="opacity: 1;" and .="{}"]'

browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
browser.set_window_size(500, 1000)
wait = WebDriverWait(browser, 10)
click = lambda el: wait.until(EC.element_to_be_clickable((By.XPATH, el))).click()

browser.get(URL)
sleep(10)
for i in range(1, 51):
    click(BOX.format(i))
    sleep(.6)

sleep(10)
browser.quit()
