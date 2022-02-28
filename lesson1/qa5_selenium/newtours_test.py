from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from time import sleep


service_chrome = Service(r"C:\Users\Gal's PC\Desktop\Selenium_Drivers\chromedriver.exe")
#service_firefox = Service(r"C:\selenium1\geckodriver.exe")

driver = webdriver.Chrome(service=service_chrome)
#driver2 = webdriver.Firefox(service=service_firefox)

driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT,"Flights").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Fli").click()

# Check that the default in "Passengers" is 1
while True:
    try:
        passengers = driver.find_element(By.NAME,"passCount")
        break
    except:
        continue

if passengers.get_attribute("value")=="1":
    print("passengers default is correct")
else:
    print("passengers default is wrong. should be 1 and it's actually",passengers.get_attribute("value"))

# Choose 2 in passengers drop down
passengers_dropdown=Select(passengers)
passengers_dropdown.select_by_visible_text("2")

# Check that the default in "Departing From" is "Acapulco
departing = driver.find_element(By.NAME,"fromPort")
if departing.get_attribute("value")=="Acapulco":
    print("departing from default is correct")
else:
    print("departing from default is wrong. should be Acapulco and it's actually", departing.get_attribute("value"))

# Choose Sydney in departing from dropdown
departing_dropdown=Select(departing)
departing_dropdown.select_by_visible_text("Sydney")

sleep(2)
driver.close()