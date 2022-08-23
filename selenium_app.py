from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(r"E:/selenium_project/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("cat")
time.sleep(2)
driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
time.sleep(1) 
# Click on Image tab
driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
# Click on first image shown 
driver.find_element(By.XPATH,'//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click()
time.sleep(2)
# Clicking on first image to full windows
driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').capture_screenshot("nda.png")
# time.sleep(2)
#Selecting particular images

# driver.find_element(By.XPATH,'//html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/a/img')

print("Run Successfully")
