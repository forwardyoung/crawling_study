from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 3초까지 기다린다 => 에러 덜어줌

url = "https://www.instagram.com/"
driver.get(url=url)

xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
time.sleep(20)