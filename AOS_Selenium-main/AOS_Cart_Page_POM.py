from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class Cart_Page:

    def __init__(self, driver: webdriver.Chrome):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, 10)

    def shopping_cart_Title(self):
        shopping_cart = self.driver.find_element(By.CSS_SELECTOR,'a[class="select  ng-binding"]')
        return shopping_cart.text

    def cart_total(self):
        self.general_wait()
        total = self.driver.find_element(By.XPATH, '//td[@colspan="2"]/span[2]')
        return total.text

    def cart_page_qty(self,row):
        qty = self.driver.find_elements(By.XPATH, '//td[@class="smollCell quantityMobile"]/label[2]')
        return qty[row].text

    def item_edit_in_cart(self,row):
        self.wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, 'table[ng-show="cart.productsInCart.length > 0"]')))
        edit = self.driver.find_elements(By.LINK_TEXT, 'EDIT')
        return edit[row]

    def checkout_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[role="button"][class="roboto-medium tami uft-class ng-binding"]')

    def general_wait(self):
        self.wait.until(EC.invisibility_of_element((By.XPATH,"//div[@class='loader']")))