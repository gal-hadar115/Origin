from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers(self):
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def laptops(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def mice(self):
        return self.driver.find_element(By.ID, 'miceImg')

    def headphones(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def go_homepage(self):
        return self.driver.find_element(By.XPATH, "//div/a[@href='#/'][@role='link']")

    def special_offer(self):
        return self.driver.find_element(By.LINK_TEXT, "SPECIAL OFFER")

    def popular_items(self):
        return self.driver.find_element(By.LINK_TEXT, "POPULAR ITEMS")

    def contact_us(self):
        return self.driver.find_element(By.LINK_TEXT, 'CONTACT US')


