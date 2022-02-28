from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Calc_Page:
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def first_number(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")

    def second_number(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")

    def operator(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[ng-model='operator']")

    def go_button(self):
        return self.driver.find_element(By.ID,"gobutton")

    def result(self):
        return self.driver.find_element(By.CSS_SELECTOR,".ng-binding")

    def type_first_number(self,num:str):
        self.first_number().send_keys(num)

    def type_second_number(self,num:str):
        self.second_number().send_keys(num)

    def click_go_button(self):
        self.go_button().click()

    def choose_operator(self,op):
        operator_dropdown=Select(self.operator())
        operator_dropdown.select_by_visible_text(op)

    def get_result(self):
        self.wait_for_result()
        return self.result().text

    def wait_for_result(self):
        while self.result().text[0] == ".":
            pass