import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys('Мой ответ')
    browser.find_element(By.CLASS_NAME, 'btn-default').click()

finally:
    time.sleep(5)
    browser.close()
