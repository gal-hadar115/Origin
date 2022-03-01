from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class Checkout:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def existing_user(self):
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    def existing_password(self):
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def login_button(self):
        return self.driver.find_element(By.ID, 'login_btnundefined')

    def sign_in_existing_account(self,user,password):
        self.existing_user().send_keys(user)
        self.existing_password().send_keys(password)
        self.login_button().click()


    def next_button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'next_btn')))
        return self.driver.find_element(By.ID, 'next_btn')

    def credit_card(self):
        return self.driver.find_element(By.NAME, 'masterCredit')

    def card_number(self):
        return self.driver.find_element(By.ID, 'creditCard')

    def cvv_number(self):
        return self.driver.find_element(By.NAME, 'cvv_number')

    def cardholder_name(self):
        return self.driver.find_element(By.NAME, 'cardholder_name')

    def credit_card_info(self,card,cvv,name):
        self.credit_card().click()
        self.card_number().send_keys(card)
        sleep(0.5)
        self.cvv_number().send_keys(cvv)
        sleep(0.5)
        self.cardholder_name().send_keys(name)

    def expiration_month(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'mmListbox')))
        month = self.driver.find_element(By.NAME, 'mmListbox')
        return Select(month)

    def expiration_year(self):
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'yyyyListbox')))
        year = self.driver.find_element(By.NAME, 'yyyyListbox')
        return Select(year)

    def pay_with_credit_card(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'pay_now_btn_ManualPayment')))
        return self.driver.find_element(By.ID, 'pay_now_btn_ManualPayment')

    def safepay_tick(self):
        return self.driver.find_element(By.NAME, 'safepay')

    def safepay_user(self):
        return self.driver.find_element(By.NAME, 'safepay_username')

    def safepay_password(self):
        return self.driver.find_element(By.NAME, 'safepay_password')

    def pay_now_button(self):
        return self.driver.find_element(By.ID, 'pay_now_btn_SAFEPAY')

    def payment_method(self,user,password):
        self.safepay_tick().click()
        self.safepay_user().send_keys(user)
        self.safepay_password().send_keys(password)
        self.pay_now_button().click()

    def payment_success(self):
        return self.driver.find_element(By.ID, 'orderPaymentSuccess')




