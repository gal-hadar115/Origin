from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service_chrome = Service(r"C:\Users\Gal's PC\Desktop\Selenium_Drivers\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/#/")
#driver.maximize_window()


# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

# driver.find_element(By.ID,'headphonesImg').click()
# sleep(3)
# while True:
#     try:
#         driver.find_element(By.LINK_TEXT,'POPULAR ITEMS').click()
#         break
#     except:
#         pass
wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'POPULAR ITEMS')))
while True:
    try:
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        break
    except:
        pass