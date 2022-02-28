from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


service_chrome = Service(r"C:\selenium1\chromedriver.exe")
#service_firefox = Service(r"C:\selenium1\geckodriver.exe")

driver = webdriver.Chrome(service=service_chrome)
#driver2 = webdriver.Firefox(service=service_firefox)

driver.get("https://www.google.com/")
driver.maximize_window()


# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

# Check that the text "Gmail" appears in the right location
gmail = driver.find_element(By.CSS_SELECTOR,"[class='gb_d'][dir='ltr']")


if gmail.text=="Gmail":
    print("test passed: Gmail appears")
else:
    print("test failed. Gmail doesn't appear. the shown text is",gmail.text)


# Get the search line element object
# driver.find_element(By.CSS_SELECTOR,".gLFyf").send_keys("selenium")
# driver.find_element(By.CSS_SELECTOR,".gLFyf").clear()
# driver.find_element(By.CSS_SELECTOR,".gLFyf").send_keys("python")
# driver.find_element(By.CSS_SELECTOR,".gLFyf").send_keys(Keys.ENTER)

#search_line = driver.find_element(By.NAME,"q")
search_line = driver.find_element(By.CSS_SELECTOR,"input[type='text']")

search_line.send_keys("selenium")
sleep(0.5)
search_line.clear()
sleep(0.5)
search_line.send_keys("python")
# Get the search button element
#search_button = driver.find_element(By.CSS_SELECTOR,".FPdoLc > center:nth-child(1) > input:nth-child(1)")
#search_button.click()

search_line.send_keys(Keys.ENTER)