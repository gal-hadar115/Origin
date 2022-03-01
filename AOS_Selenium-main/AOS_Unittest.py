from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from AOS_HomePage_POM import HomePage
from AOS_Categories_POM import Categories
from AOS_Items_POM import Items
from AOS_Cart_Window_POM import Cart_Window
from AOS_Cart_Page_POM import Cart_Page
from AOS_Ceate_User_POM import Create_User
from AOS_Checkout_POM import Checkout
from AOS_My_Orders_POM import My_Orders
from selenium.webdriver.support.select import Select

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
        self.cart = Cart_Window(self.driver)
        self.cart_page = Cart_Page(self.driver)
        self.create_user =Create_User(self.driver)
        self.checkout = Checkout(self.driver)
        self.my_orders = My_Orders(self.driver)

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
        """ This test verifies that the name, color, quantity, and the price match with the information entered
        The way the cart is handled is it stacks the products in an order from newest added to oldest """
        # Adding 2 black mice
        self.homepage.mice().click()
        self.categories.mice_items(0)
        sleep(1)
        self.items.item_flow(2, 'BLACK')
        sleep(1)
        self.assertIn('HP USB 3 BUTTON OPTICAL MOUSE',self.cart.cart_items_name(0))
        self.assertIn('2',self.cart.cart_items_quantity(0))
        self.assertEqual(self.cart.cart_items_color(0),'BLACK')
        self.assertIn(self.cart.cart_items_price(0),self.cart.price_calculator(0))
        # Adding 3 GRAY speakers
        self.homepage.homepage_icon().click()
        self.homepage.speakers().click()
        self.categories.speakers_items(0)
        sleep(1)
        self.items.item_flow(3, 'GRAY')
        sleep(1)
        self.assertIn('BOSE SOUNDLINK BLUETOOTH', self.cart.cart_items_name(0))
        self.assertIn('3',self.cart.cart_items_quantity(0))
        self.assertEqual(self.cart.cart_items_color(0), 'GRAY')
        self.assertIn(self.cart.cart_items_price(0), self.cart.price_calculator(0))
        # Adding 4 black TABLETS
        self.homepage.homepage_icon().click()
        self.homepage.tablets().click()
        self.categories.headphones_items(0)
        sleep(1)
        self.items.item_flow(4,'BLACK')
        sleep(1)
        self.assertIn('HP ELITEPAD 1000 G2 TABLET', self.cart.cart_items_name(0))
        self.assertIn('4', self.cart.cart_items_quantity(0))
        self.assertEqual(self.cart.cart_items_color(0), 'BLACK')
        self.assertIn(self.cart.cart_items_price(0), self.cart.price_calculator(0))

    def test_remove_item(self):
        """ This test checks that removing an item for the cart window was actually removed """
        self.homepage.laptops().click()
        self.categories.laptops_items(0)
        sleep(1)
        self.items.item_flow(2, 'BLACK')
        sleep(1)
        self.homepage.homepage_icon().click()
        self.homepage.headphones().click()
        self.categories.headphones_items(2)
        sleep(1)
        self.items.item_flow(3, 'YELLOW')
        sleep(1)
        self.cart.remove_item(1)
        self.assertNotIn('HP H2310 IN-EAR HEADSET',self.cart.table_items())

    def test_go_to_cart_page(self):
        """ This test checks that by clicking the cart button it takes us to the shopping cart page and the title
         'shopping cart' appears in the top left"""
        self.homepage.tablets().click()
        self.categories.tablets_items(1)
        self.items.item_flow(1,'GRAY')
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.shopping_cart_Title(),'SHOPPING CART')

    def test_total_price_cart_page(self):

        self.homepage.speakers().click()
        self.categories.speakers_items(1)
        self.items.item_flow(1,'TURQUOISE')
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(4)
        self.items.item_flow(2,'GRAY')
        self.homepage.homepage_icon().click()
        self.homepage.laptops().click()
        self.categories.laptops_items(6)
        self.items.item_flow(3,'PURPLE')
        self.cart.cart_button().click()

    def test_quantity(self):
        self. homepage.mice().click()
        self.categories.mice_items(1)
        self.items.item_flow(1,'RED')
        self.homepage.homepage_icon().click()
        self.homepage.laptops().click()
        self.categories.laptops_items(7)
        self.items.item_flow(2,'GRAY')
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.cart_page_qty(0),'2')
        self.assertEqual(self.cart_page.cart_page_qty(1), '1')
        self.cart_page.item_edit_in_cart(0).click()
        self.items.change_quantity(1)
        self.items.add_to_cart().click()
        self.cart.cart_button().click()
        self.cart_page.item_edit_in_cart(1).click()
        self.items.change_quantity(2)
        self.items.add_to_cart().click()
        self.cart.cart_button().click()
        self.assertEqual(self.cart_page.cart_page_qty(0),'1')
        self.assertEqual(self.cart_page.cart_page_qty(1), '2')

    def test_back_function(self):
        self.homepage.tablets().click()
        self.categories.tablets_items(0)
        self.driver.back()
        self.assertEqual(self.driver.current_url,'https://advantageonlineshopping.com/#/category/Tablets/3')
        self.driver.back()
        self.assertEqual(self.driver.current_url,'https://advantageonlineshopping.com/#/')

    def test_checkout_process(self):
        self.homepage.tablets().click()
        self.categories.tablets_items(0)
        self.items.item_flow(1,'BLACK')
        self.homepage.homepage_icon().click()
        self.homepage.headphones().click()
        self.categories.headphones_items(2)
        self.items.item_flow(1,'WHITE')
        self.cart.cart_button().click()
        self.cart_page.checkout_button().click()
        self.create_user.registration_button().click()
        self.create_user.account_details('bigfoot','Aa123456','Aa123456','asdf@gmail.com')
        self.create_user.register_button().click()
        self.checkout.next_button().click()
        self.checkout.payment_method('asdfasd','Aa123456')
        self.assertTrue(self.checkout.payment_success())
        sleep(1)
        self.homepage.account_icon().click()
        self.my_orders.my_orders_button().click()
        self.assertEqual(self.cart.cart_total_items(),'0')
        self.assertTrue(self.my_orders.order_number())

    def test_checkout_w_existing_account(self):
        self.homepage.laptops().click()
        self.categories.laptops_items(8)
        self.items.item_flow(1, 'PURPLE')
        self.homepage.homepage_icon().click()
        self.homepage.mice().click()
        self.categories.mice_items(3)
        self.items.item_flow(1, 'PURPLE')
        self.cart.cart_button().click()
        self.cart_page.checkout_button().click()
        self.checkout.sign_in_existing_account('asdasd', 'Aa123456')
        self.checkout.next_button().click()
        self.checkout.credit_card_info('1234567890987654','4231','bigfoot b')
        self.checkout.expiration_month().select_by_visible_text('01')
        self.checkout.expiration_year().select_by_visible_text('2025')
        self.checkout.pay_with_credit_card().click()
        self.assertTrue(self.checkout.payment_success())
        sleep(1)
        self.homepage.account_icon().click()
        self.my_orders.my_orders_button().click()
        self.assertEqual(self.cart.cart_total_items(), '0')
        self.assertTrue(self.my_orders.order_number())









    def tearDown(self):
        self.driver.quit()