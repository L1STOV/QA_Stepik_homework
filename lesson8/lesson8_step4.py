import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://SunInJuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    x = int(browser.find_element(By.ID, 'input_value').text)
    result = math.log(abs(12 * math.sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(str(result))
    browser.find_element(By.ID, 'robotCheckbox').click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()

finally:
    time.sleep(2)
    browser.close()
