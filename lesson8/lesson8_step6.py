import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(2)').send_keys('Spartak')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)').send_keys('Listov')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)').send_keys('spartak99@mail.ru')
    browser.find_element(By.ID, 'file').send_keys(file_path)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(1)
    browser.close()
