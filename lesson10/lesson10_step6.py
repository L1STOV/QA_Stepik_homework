from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://suninjuly.github.io/cats.html'
browser = webdriver.Chrome()

try:
    browser.get(url)
    browser.implicitly_wait(5)
    browser.find_element_by_id("button")
finally:
    browser.close()
