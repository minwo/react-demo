from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# 브라우저 꺼짐 방지 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# 특정 문구
text = "Hello, World!"
text2 = "Hello, World!"

# chromedriver
# 압축해제한 웹드라이버의 경로와 파일명 지정
driver = webdriver.Chrome()

# page 1 ---------------------------------------------------------------------------------------------------
driver.get("https://gamedori.xyz/jaub")

# id ps
driver.find_element(By.ID, 'uid').send_keys('rotoflals')
driver.find_element(By.ID, 'upw').send_keys('lee8670!')

time.sleep(2)

driver.find_element(By.CLASS_NAME, 'button').click()

time.sleep(10000)
driver.find_element(By.CLASS_NAME, 'ab-btn-write').click()

time.sleep(2)

driver.find_element(By.CLASS_NAME, 'wf-input').send_keys(text)

time.sleep(5)
iframe = driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
driver.switch_to.frame(iframe)
driver.find_element(By.CLASS_NAME, 'rhymix_content').send_keys(text2)

# driver.find_element(By.ID, 'cmd_reg').click()
# driver.find_element(By.NAME, 'title').send_keys(text)

