from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


service_chrome = Service(r"C:\selenium1\chromedriver.exe")
#service_firefox = Service(r"C:\selenium1\geckodriver.exe")

driver = webdriver.Chrome(service=service_chrome)
#driver2 = webdriver.Firefox(service=service_firefox)

driver.get("https://juliemr.github.io/protractor-demo/")
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
#driver.implicitly_wait(10)

# First number
num1 = driver.find_element(By.CSS_SELECTOR,"[ng-model='first']")
num1.send_keys("15")

# Operator
operator = driver.find_element(By.CSS_SELECTOR,"[ng-model='operator']")
op_dropdown = Select(operator)
#op_dropdown.select_by_visible_text("*")
#op_dropdown.select_by_value("MULTIPLICATION")
op_dropdown.select_by_index(3)

# second number
num2 = driver.find_element(By.CSS_SELECTOR,"[ng-model='second']")
num2.send_keys("2")

# Click Go
go = driver.find_element(By.ID,"gobutton")
go.click()

# Check result
result = driver.find_element(By.CSS_SELECTOR,".ng-binding")

while result.text[0]==".":
    pass

# wait = WebDriverWait(driver,10)
# locator_tuple=(By.CSS_SELECTOR,"td.ng-binding")
# wait.until(EC.visibility_of_element_located(locator_tuple))


if result.text=="30":
    print("test passed")
else:
    print("test failed. result is:",result.text)

driver.close()