import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url_old = 'http://suninjuly.github.io/registration1.html'
url_new = 'http://suninjuly.github.io/registration2.html'

try:
    browser.get(url_new)
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')
    input3.send_keys("ivanpetrov@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.first_class > input')
    input4.send_keys("7044221312")
    input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block > div.form-group.second_class > input')
    input5.send_keys("пр.Ленина")

    browser.find_element(By.CLASS_NAME, 'btn-default').click()

finally:
    time.sleep(1)
    browser.close()
