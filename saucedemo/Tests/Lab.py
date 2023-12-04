from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
import os
from saucedemo.Pages.swag import swag


class swag_test(unittest.TestCase):
    currenct_working_directory = os.getcwd()

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.currenct_working_directory + '\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def test_swag(self):
        driver = self.driver
        text = swag(driver)
        text.username("standard_user")
        text.password("secret_sauce")
        text.lon()
        text.cart()
        text.filter()
        text.remove()
        text.hamburger()
        text.logout()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
    if __name__ == '__main__':
        unittest.main()
