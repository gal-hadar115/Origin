from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from AOS_HomePage_POM import HomePage
from AOS_Categories_POM import Categories
from AOS_Items_POM import Items
from AOS_Cart_POM import Cart

class AOS_UnitTests(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\Users\Gal's PC\Desktop\Selenium_Drivers\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://advantageonlineshopping.com/#/")
        #self.driver.maximize_window()

        # In case an element is not found on the page, will try again for 10 seconds
        # before we get an error message
        self.driver.implicitly_wait(10)

        self.homepage = HomePage(self.driver)
        self.categories = Categories(self.driver)
        self.items = Items(self.driver)
        self.cart = Cart(self.driver)

    def test_items_in_cart(self):
        """ This test checks that the right amount of items are in the cart"""
        self.homepage.speakers().click()
        self.categories.speakers_items(1)
        sleep(1)
        self.items.item_flow(2,'RED')
        sleep(1)
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(0)
        sleep(1)
        self.items.item_flow(3,'BLACK')
        sleep(1)
        self.assertEqual(self.cart.cart_total_items(), '5')

    def test_items_info_in_cart(self):
        """ This test verifies that the name, color, quantity, and the price match with the information entered """
        self.homepage.speakers().click()
        self.categories.speakers_items(1)
        sleep(1)
        self.items.item_flow(2, 'RED')
        sleep(1)
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(0)
        sleep(1)
        self.items.item_flow(3, 'BLACK')
        sleep(1)
        self.homepage.homepage_icon().click()
        self.categories.headphones_items(0)
        sleep(1)
        self.items.item_flow(4,'BLACK')
        sleep(1)
        self.assertEqual(self.cart.cart_items_name(),)