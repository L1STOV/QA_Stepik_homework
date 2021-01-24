import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)
    result = x + y
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(result))
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(2)
    browser.close()
