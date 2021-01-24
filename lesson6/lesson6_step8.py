import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

url = 'http://suninjuly.github.io/find_xpath_form'
browser = webdriver.Chrome()

try:
    browser.get(url)

    input1 = browser.find_element_by_css_selector('body > div > form > div:nth-child(1) > input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('body > div > form > div:nth-child(2) > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('body > div > form > div:nth-child(3) > input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    browser.find_element(By.XPATH, '/html/body/div/form/div[6]/button[3]').click()

except NoSuchElementException:
    print(NoSuchElementException)

finally:
    browser.close()
