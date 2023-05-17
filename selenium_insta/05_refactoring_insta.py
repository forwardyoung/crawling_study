from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(5) # 5초까지 기다린다 => 에러 덜어줌

url = "https://www.instagram.com/"
driver.get(url=url)

def login(id, password):
    input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER) # div 안에 button XPath

# Search
def search(hashtag, scroll_times):
    url = f"https://www.instagram.com/explore/tags/{hashtag}"
    driver.get(url=url)
    time.sleep(6) # 해시태그 검색 후 기다린 후 page_source 보기
    # print(driver.page_source)

    for _ in range(scroll_times): # 스크롤 5번
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

# 좋아요 댓글
def like_comment(nth, comment, repeat=3):
    row = (nth - 1) // 3 + 1 # n번째 포스트가 몇 번째 행인지 계산
    col = (nth - 1) % 3 + 1 # n번째 포스트가 몇 번째 열인지 계산

    # n번째 포스트 클릭
    # full xpath 복사
    xpath = f'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{row}]/div[{col}]'
    driver.find_element(By.XPATH, xpath).click()

    for _ in range(repeat):
        # like
        like_xpath = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button'
        driver.find_element(By.XPATH, like_xpath).click()

        # comment - textarea xpath 복사
        comment_xpath ='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        # 게시 버튼 누르기
        comment_button_xpath = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[3]/div/div/section[3]/div/form/div/div[2]/div'
        driver.find_element(By.XPATH, comment_button_xpath).click()

        # 다음 게시물 버튼 누르기
        next_button_xpath = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button'
        driver.find_element(By.XPATH, next_button_xpath).click()

id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")
login(id, password)

time.sleep(5)

# Search
hashtag = "고양이"
search(hashtag, 0)

# like comment
like_comment(6, "귀여워요", 2) # n번째 포스트 클릭
