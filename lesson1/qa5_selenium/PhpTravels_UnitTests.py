from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from qa5_selenium.Php_Login_Page import Php_Login_Page
from qa5_selenium.Php_Dashboard_Page import Php_Dashboard_Page

class PhpTravels_UnitTests(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://phptravels.net/api/admin")
        self.driver.maximize_window()

        # In case an element is not found on the page, will try again for 10 seconds
        # before we get an error message
        self.driver.implicitly_wait(10)
        self.login_page = Php_Login_Page(self.driver)
        self.dashboard_page = Php_Dashboard_Page(self.driver)

    def test_dashboard(self):
        """ This test is checking that after login the DASHBOARD text appears correctly"""
        # self.login_page.type_user("admin@phptravels.com")
        # self.login_page.type_password("demoadmin")
        # self.login_page.login_click()
        self.login_page.login("admin@phptravels.com","demoadmin")

        self.assertEqual(self.dashboard_page.dashboard_text(),"DASHBOARD")

    def test_logout(self):
        """This test is checking that the logout returns to login page"""
        self.login_page.type_user("admin@phptravels.com")
        self.login_page.type_password("demoadmin")
        self.login_page.login_click()

        self.dashboard_page.logout()

        self.assertEqual(self.login_page.login_title_text(),"Login")

    def tearDown(self):
        self.driver.close()