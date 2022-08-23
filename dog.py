from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("E:/selenium_project/chromedriver_win32/chromedriver.exe")
driver.maximize_window
driver.get("https://google.com/")
driver.find_element(By.NAME,"q").send_keys("Dog")
driver.find_element(By.CLASS_NAME)