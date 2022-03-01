from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from AOS_HomePage_POM import HomePage
from AOS_Categories_POM import Categories
from AOS_Items_POM import Items
from AOS_Cart_Window_POM import Cart_Window
from AOS_Cart_Page_POM import Cart_Page
from AOS_My_Orders_POM import My_Orders

service_chrome = Service(r"C:\Users\Gal's PC\Desktop\Selenium_Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)

homepage = HomePage(driver)
categories = Categories(driver)
item = Items(driver)
cart = Cart_Window(driver)
cart_page = Cart_Page(driver)
my_orders = My_Orders(driver)
driver.get("https://advantageonlineshopping.com/#/")
#driver.maximize_window()

driver.implicitly_wait(10)

# printing all the available speakers
#homepage.speakers().click()
# categories.speakers_info()
#
# # adding 2 Red Bose soundlink wireless speaker to cart
# categories.speakers_items(1)
# item.colors_info()
# item.change_quantity(2)
# sleep(1)
# item.choose_color('RED')
# sleep(1)
# item.add_to_cart().click()
# sleep(1)
#
# # Going to mice category
# homepage.homepage_icon().click()
# homepage.mice().click()
# categories.mice_info()
#
# # adding 3 Blue Logitech mice to cart
# categories.mice_items(7)
# item.choose_color('BLUE')
# sleep(1)
# item.change_quantity(3)
# sleep(1)
# item.add_to_cart().click()
# sleep(0.5)
# Check that the cart quantity matches to the amount of items added to the cart
# if cart.cart_items_from_nav()=='5':
#     print('Test passed')
# else:
#     print(f'Test failed! There are {cart.cart_items_from_nav()} items in cart instead')

# homepage.tablets().click()
# categories.tablets_items(1)
# item.item_flow(2,'BLACK')
# cart.cart_button().click()
# print(cart_page.cart_page_qty(0))
# sleep(1)
# cart_page.item_edit_in_cart(0).click()
# sleep(1)
# item.change_quantity(1)
# sleep(1)
# cart.cart_button().click()
# print(cart_page.cart_page_qty(0))







