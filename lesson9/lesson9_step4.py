import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    browser.find_element(By.TAG_NAME, 'button').click()
    browser.switch_to.window(browser.window_handles[1])
    print(browser.find_element(By.ID, 'input_value').text)
    x = browser.find_element(By.ID, 'input_value').text
    result = math.log(abs(12 * math.sin(int(x))))
    browser.find_element(By.ID, 'answer').send_keys(str(result))
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.switch_to.alert.text)
    browser.close()

finally:
    time.sleep(1)
    browser.close()
