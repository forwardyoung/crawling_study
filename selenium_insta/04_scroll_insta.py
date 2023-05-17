from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 3초까지 기다린다 => 에러 덜어줌

url = "https://www.instagram.com/"
driver.get(url=url)


id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")
input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
input_id.send_keys(id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER) # div 안에 button XPath


time. sleep(3) # 로그인 후 3초 정도 기다린 후 search로

# Search
hashtag = "강아지"
url = f"https://www.instagram.com/explore/tags/{hashtag}"
driver.get(url=url)
time.sleep(6) # 해시태그 검색 후 기다린 후 page_source 보기
# print(driver.page_source)

for _ in range(5): # 스크롤 5번
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)

time.sleep(100)

