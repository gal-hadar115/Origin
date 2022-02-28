from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Php_Dashboard_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def dashboard_title(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[class='container-fluid px-4']>a>div")

    def dropdown_icon(self):
        return self.driver.find_element(By.ID,"dropdownMenuProfile")

    def logout_button(self):
        list_elements = self.driver.find_elements(By.CSS_SELECTOR, "[class='me-3']")
        return list_elements[-1]

    def dashboard_text(self):
        return self.dashboard_title().text

    def drop_down_icon_click(self):
        self.wait_for_logout_icon()
        self.dropdown_icon().click()

    def wait_for_logout_icon(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class='bodyload']")))

    def logout_click(self):
        self.logout_button().click()

    def logout(self):
        self.drop_down_icon_click()
        self.logout_click()