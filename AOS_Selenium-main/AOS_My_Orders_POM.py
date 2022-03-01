from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class My_Orders:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def my_orders_button(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div/label[@class="option ng-scope"][@translate="My_Orders"][@href="javascript:void(0)"]')))
        return self.driver.find_element(By.XPATH, '//div/label[@class="option ng-scope"][@translate="My_Orders"][@href="javascript:void(0)"]')

    def order_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'label[class="left ng-binding"]')