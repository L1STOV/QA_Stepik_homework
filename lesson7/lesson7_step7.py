import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    chest = browser.find_element(By.TAG_NAME, 'img')
    x = int(chest.get_attribute('valuex'))
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(str(result))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(1)
    browser.close()
