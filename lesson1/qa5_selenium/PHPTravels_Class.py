from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


#service_chrome = Service(r"C:\selenium1\chromedriver.exe")
service_firefox = Service(r"C:\selenium1\geckodriver.exe")

#driver = webdriver.Chrome(service=service_chrome)
driver = webdriver.Firefox(service=service_firefox)

driver.get("https://phptravels.net/api/admin")
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

# Type User
user = driver.find_element(By.CSS_SELECTOR,"[name='email'][type='text']")
user.send_keys("admin@phptravels.com")
print(user.get_attribute("value"))

# Type password
password = driver.find_element(By.NAME,"password")
password.send_keys("demoadmin")

# Click Login
login_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
login_button.click()

# Check Dashboard text
dashboard = driver.find_element(By.CSS_SELECTOR,"[class='container-fluid px-4']>a>div")
if dashboard.text=="DASHBOARD":
    print("text passed")
else:
    print("teat failed")

# Click on the icon for logout
wait = WebDriverWait(driver,10)

# wait.until(EC.element_to_be_clickable((By.ID,"dropdownMenuProfile")))
# wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"div[class='bodyload']")))

while True:
    try:
        driver.find_element(By.ID,"dropdownMenuProfile").click()
        break
    except:
        pass

# Click on Logout (the 4th element in the list, according to the html)
#list_elements = driver.find_elements(By.CSS_SELECTOR,"[class='me-3']")
#print(len(list_elements))
#list_elements[-1].click()
driver.find_element(By.XPATH,"//div[text()='Logout']").click()


# Go back to previous page
#driver.back()

# Close the browser
driver.close()