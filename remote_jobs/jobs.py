# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://jobs.dou.ua/companies/expoplatform/vacancies/143344/?from=list_hot'

browser = webdriver.Chrome()
browser.get(url)

position = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div/h1').text
company = browser.find_element(By.XPATH, '//div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/a[1]').text

city = browser.find_element(By.CLASS_NAME, 'place').text
salary = browser.find_element(By.CLASS_NAME, 'salary').text

skills_title = browser.find_element(By.CLASS_NAME, 'g-h3').text
skills = browser.find_element(By.CLASS_NAME, 'vacancy-section').text

responsibilities_title = browser.find_element(By.CSS_SELECTOR, 'h3:nth-child(8)').text

responsibilities = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(9) > p').text

offers_title = browser.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[1]/div/div[4]/h3[3]').text

offers = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(7)').text

time.sleep(1)
browser.close()
