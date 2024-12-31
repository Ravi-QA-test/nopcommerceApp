from itertools import count

import pytest
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGenerate
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import CustomersPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
import time

class TestSearchCustomer_003:
    baseURL = ReadConfig.getAppplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerate.loggen()

    @pytest.mark.regression
    def test_search_customer(self, setup):
        self.logger.info("********** test_add_new_customer **********")
        self.driver = setup  # browser 'driver' object returned from "conftest.py' stores here.
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(4)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        self.logger.info("********** Login Success **********")

        self.logger.info("********* Starting Add New Customer Test... *********")

        self.cus_page = CustomersPage(self.driver)
        self.cus_page.click_on_customers_menu()
        self.logger.info("********** Clicked 'Customers' Menu... **********")
        self.cus_page.click_on_customers_menuitem()
        self.logger.info("********** Clicked Sub Menu 'Customers'... **********")

        self.search_cus_page = SearchCustomerPage(self.driver)
        # If the downward arrow element is not present, then it'll skip the step(pass) and run the test.
        try:
            self.search_cus_page.click_downwards_arrow()
        except:
            pass
        self.search_cus_page.set_search_firstname("James")
        self.search_cus_page.click_on_search()

        self.fname = self.search_cus_page.search_cus_by_firstname()
        self.count = sum(item.count('James') for item in self.fname)

        if any('James' in name for name in self.fname):
            # if "James" in self.fname:
            assert True
            self.logger.info(f"Table name = {self.fname}")
            self.logger.info(f"Count = {self.count}")
            self.driver.close()
            self.logger.info("****** Test Case 'test_search_customer' is Passed! ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\SearchCustomer\\test_search_cus_by_fname.png")
            self.logger.error(f"{self.count} matches for name 'James'")
            self.driver.close()
            self.logger.error("****** Test Case 'test_search_customer' is Failed! ******")
            assert False
