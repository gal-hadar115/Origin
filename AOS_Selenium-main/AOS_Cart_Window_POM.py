from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


class Cart_Window:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def cart_total_items(self):
        '''Find the current amount of items in the cart from the navigation bar'''
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')))
            total_items = self.driver.find_element(By.XPATH,'//li[@data-ng-mouseenter="enterCart()"][@data-ng-mouseleave="leaveCart()"]/a[@class="img"]/span')
            return total_items.text

        except TimeoutException:
            return '0'

    def cart_items_name(self,row):
        self.hover()
        name = self.driver.find_elements(By.CSS_SELECTOR, 'h3[class="ng-binding"]')
        return name[row].text

    def cart_items_quantity(self,row):
        self.hover()
        qty = self.driver.find_elements(By.XPATH, '//a/label[1]')
        return qty[row].text

    def cart_items_color(self,row):
        self.hover()
        color = self.driver.find_elements(By.XPATH, '//a/label/span')
        return color[row].text

    def cart_items_price(self,row):
        self.hover()
        price = self.driver.find_elements(By.XPATH, "//p[@class='price roboto-regular ng-binding']")
        return price[row].text

    def price_calculator(self, row):
        self.hover()
        money = self.driver.find_element(By.XPATH, "//div[@id='Description']/h2[@class='roboto-thin screen768 ng-binding']")
        price = money.text[1:]
        if ',' in price:
           price = price.replace(',', '')
        qty = self.cart_items_quantity(row)
        qty = qty[4:]
        total = float(price)*int(qty)
        return "${:,.2f}".format(total)

    def price_cart_window_summary(self):
        self.hover()
        price = self.driver.find_elements(By.XPATH, "//p[@class='price roboto-regular ng-binding']")



    def hover(self):
        hover = self.driver.find_element(By.ID, "shoppingCartLink")
        self.action.move_to_element(hover).perform()

    def remove_item(self,row):
        x = self.driver.find_elements(By.CSS_SELECTOR,'.removeProduct')
        return x[row]

# this function finds the name, qty, color, and price for all items in the cart
    def table_items(self):
        self.hover()
        try:
            table = self.driver.find_element(By.CSS_SELECTOR, 'table[ng-show="cart.productsInCart.length > 0"]')
            tr = self.driver.find_elements(By.CSS_SELECTOR, "tr[id='product']")
            td = table.find_elements(By.TAG_NAME, 'td')
            for i in td[:-3]:
                return i.text
        except ElementNotInteractableException:
            return 'Table not found'

# this function finds the name, qty, color, and price of a single item in cart
    def row_finder(self, row):
        self.hover()
        try:
            table = self.driver.find_element(By.CSS_SELECTOR, 'table[ng-show="cart.productsInCart.length > 0"]')
            tr = self.driver.find_elements(By.CSS_SELECTOR, "tr[id='product']")
            return tr[row].text

        except ElementNotInteractableException:
            return 'Table not found'

    def cart_button(self):
        return self.driver.find_element(By.ID,'menuCart')
