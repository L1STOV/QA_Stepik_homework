import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(url)

    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value').text
    result = math.log(abs(12 * math.sin(int(x))))
    browser.find_element(By.ID, 'answer').send_keys(str(result))
    browser.find_element(By.ID, 'solve').click()

finally:
    browser.close()
