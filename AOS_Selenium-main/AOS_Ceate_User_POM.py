from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class Create_User:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def registration_button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'registration_btnundefined')))
        return self.driver.find_element(By.ID,'registration_btnundefined')

    def username(self):
        return self.driver.find_element(By.CSS_SELECTOR,'input[name="usernameRegisterPage"][type="text"]')

    def password(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="passwordRegisterPage"][type="password"]')

    def confirm_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="confirm_passwordRegisterPage"][type="password"]')

    def email(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="emailRegisterPage"][type="text"]')

    def terms(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'label[style="display: block;"]')

    def register_button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, 'register_btnundefined')))
        return self.driver.find_element(By.ID, 'register_btnundefined')

    def account_details(self,user,password,conf_pass,email):
        self.username().send_keys(user)
        self.password().send_keys(password)
        self.confirm_password().send_keys(conf_pass)
        self.email().send_keys(email)
        self.terms().click()






