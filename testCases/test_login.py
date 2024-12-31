import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerate
import time

class TestLogin_001:

    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getAppplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerate.loggen()

    # Before executing the 'test_home_page_title' method, setup method will execute.
    # In setup method, we did the browser initialization part and it was in 'conftest.py' file.

    @pytest.mark.sanity
    def test_home_page_title(self, setup):

        self.logger.info("********** test_test_home_page_title **********")
        # Replaced, driver = webdriver.Chrome() with, self.driver = setup, as below.
        self.driver = setup         # browser 'driver' object returned from "conftest.py' stores here.
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(4)

        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** Test Case 'test_home_page_title' is Passed! ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_home_page_title.png")
            # Above,  '.' is used to indicate that the folder is in current project (.\\Screenshots)
            self.driver.close()
            self.logger.error("****** Test Case 'test_home_page_title' is Failed! ******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("********** test_login **********")
        # Replaced, driver = webdriver.Chrome() with, self.driver = setup, as below.
        self.driver = setup      #'driver' object returned from "conftest.py' stores here.
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****** Test Case 'test_login' is Passed! ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            # Above,  '.' is used to indicate that the folder is in current project (.\\Screenshots)
            self.driver.close()
            self.logger.error("****** Test Case 'test_login' is Failed! ******")
            assert False


        
