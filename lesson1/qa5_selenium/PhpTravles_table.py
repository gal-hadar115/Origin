from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


service_chrome = Service(r"C:\selenium1\chromedriver.exe")
#service_firefox = Service(r"C:\selenium1\geckodriver.exe")

driver = webdriver.Chrome(service=service_chrome)
#driver = webdriver.Firefox(service=service_firefox)

driver.get("https://phptravels.net/api/admin")
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

# Type User
user = driver.find_element(By.CSS_SELECTOR,"[name='email'][type='text']")
user.send_keys("admin@phptravels.com")

# Type password
while True:
    try:
        password = driver.find_element(By.NAME,"password")
        password.send_keys("demoadmin")
        break
    except:
        pass


# Click Login
login_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
login_button.click()

# Click on Booking
booking = driver.find_element(By.LINK_TEXT,"Bookings")
booking.click()

# Find the table element
table = driver.find_element(By.CSS_SELECTOR,"table#data")

# Get all the tr's of the table
tr_list = table.find_elements(By.TAG_NAME,"tr")

print(len(tr_list))

# Get the last tr
last_tr = tr_list[-1]

# Get all the td's of the last row
td_list = last_tr.find_elements(By.TAG_NAME,"td")

# Display the 9th td (the price)
print(td_list[8].text)

# ====================================================================
# Display all the prices of the table
for row in tr_list:
    td_list = row.find_elements(By.TAG_NAME, "td")
    if len(td_list)>0:
        print(td_list[8].text)


driver.close()