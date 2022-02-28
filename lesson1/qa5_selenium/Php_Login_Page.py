from selenium import webdriver
from selenium.webdriver.common.by import By

class Php_Login_Page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def user(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[name='email'][type='text']")

    def password(self):
        return self.driver.find_element(By.NAME,"password")

    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

    def type_user(self,user_name):
        self.user().send_keys(user_name)

    def type_password(self,password):
        while True:
            try:
                self.password().send_keys(password)
                break
            except:
                pass


    def login_click(self):
        self.login_button().click()

    def login_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,".display-5>strong")

    def login_title_text(self):
        return self.login_title().text

    def login(self,user,password):
        self.type_user(user)
        self.type_password(password)
        self.login_click()