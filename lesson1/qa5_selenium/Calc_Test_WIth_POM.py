from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from qa5_selenium.Calc_Page import Calc_Page

service_chrome = Service(r"C:\selenium1\chromedriver.exe")
#service_firefox = Service(r"C:\selenium1\geckodriver.exe")

driver = webdriver.Chrome(service=service_chrome)
#driver2 = webdriver.Firefox(service=service_firefox)

driver.get("https://juliemr.github.io/protractor-demo/")
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

# Create a page object
calc_page = Calc_Page(driver)

# Check if the first and second numbers are empty by default
if calc_page.first_number().get_attribute("value")=="":
    print("correct default for first number")

calc_page.type_first_number("20")
calc_page.type_second_number("6")
calc_page.choose_operator("*")
calc_page.click_go_button()

if calc_page.get_result()=="120":
    print("test passed")
else:
    print("test failed")

driver.close()