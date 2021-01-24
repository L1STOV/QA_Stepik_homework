import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    x_value = browser.find_element(By.ID, 'input_value').text
    result = math.log(abs(12 * math.sin(int(x_value))))
    print(result, type(result))
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(str(result))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(2)
    browser.close()
