import math
import time
from selenium import webdriver

url = 'http://suninjuly.github.io/find_link_text'
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
browser = webdriver.Chrome()

try:
    browser.get(url)
    browser.find_element_by_link_text(link_text).click()

    input1 = browser.find_element_by_css_selector('body > div > form > div:nth-child(1) > input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('body > div > form > div:nth-child(2) > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('body > div > form > div:nth-child(3) > input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
finally:
    browser.close()



