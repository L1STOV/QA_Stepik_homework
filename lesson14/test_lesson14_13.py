import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLesson(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.close()

    def test_first(self):
        browser = self.browser
        browser.get('http://suninjuly.github.io/registration1.html')
        browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('ddd')
        browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('qqq')
        browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input').send_keys('aaa')
        browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('zzz')
        browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input').send_keys('bbb')
        browser.find_element(By.TAG_NAME, 'button').click()
        browser.implicitly_wait(5)
        text_needed = browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(text_needed, 'Congratulations! You have successfully registered!')

    def test_second(self):
        browser = self.browser
        browser.get('http://suninjuly.github.io/registration2.html')
        browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input').send_keys('ppp')
        browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input').send_keys('mmm')
        browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input').send_keys('222')
        browser.find_element(By.XPATH, '/html/body/div/form/div[22]/div[2]/input').send_keys('111')
        browser.implicitly_wait(5)
        text_needed = browser.find_element(By.CSS_SELECTOR, 'body > div > h1').text
        self.assertEqual(text_needed, 'Congratulations! You have successfully registered!')


if __name__ == '__main__':
    unittest.main()
