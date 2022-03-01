from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


class Cart:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def cart_total_items(self):
        '''print the current amount of items in the cart from the navigation bar'''
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')))
            total_items = self.driver.find_element(By.XPATH,'//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')
            return total_items.text

        except TimeoutException:
            return '0'

    def cart_items_name(self):
        self.hover()
        return self.driver.find_element(By.CSS_SELECTOR, 'h3[class="ng-binding"]').text

    def cart_items_quantity(self):
        self.hover()
        return self.driver.find_element(By.XPATH, '//a/label[1]').text

    def cart_items_color(self):
        self.hover()
        return self.driver.find_element(By.XPATH, '//a/label/span').text

    def cart_items_price(self):
        self.hover()
        return self.driver.find_element(By.XPATH, "//p[@class='price roboto-regular ng-binding']").text

    def hover(self):
        hover = self.driver.find_element(By.ID, "shoppingCartLink")
        self.action.move_to_element(hover).perform()

