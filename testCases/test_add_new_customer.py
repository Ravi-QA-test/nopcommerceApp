import pytest
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGenerate
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.CustomersPage import CustomersPage
from pageObjects.AddNewCustomerPage import AddNewCustomerPage
import time

class TestAddNewCustomer_002:

    baseURL = ReadConfig.getAppplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerate.loggen()

    # Before executing the 'test_add_new_customer' method, setup method will execute.
    # In setup method, we did the browser initialization part and it was in 'conftest.py' file.

    @pytest.mark.sanity
    def test_add_new_customer(self, setup):

        self.logger.info("********** test_add_new_customer **********")
        self.driver = setup         # browser 'driver' object returned from "conftest.py' stores here.
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

        self.addnewcus_page = AddNewCustomerPage(self.driver)
        self.addnewcus_page.click_on_add_new_customer()
        self.logger.info("********* Clicked 'Add New Customer' button... *********")
        self.logger.info("********** Providing Add New Customer Info... **********")

        self.email = AddNewCustomerPage.generate_random_email()
        self.addnewcus_page.set_email(self.email)
        self.addnewcus_page.set_password("Chris123#")
        self.addnewcus_page.set_firstname("Chris")
        self.addnewcus_page.set_lastname("Gayle")
        self.addnewcus_page.select_gender()
        self.addnewcus_page.select_dob("09/01/1996")
        self.addnewcus_page.set_company("IFS")
        self.addnewcus_page.click_on_istaxexempt()
        self.addnewcus_page.select_newsletter("Test store 2")
        self.addnewcus_page.select_customer_roles("Vendors")
        self.addnewcus_page.select_vendor()
        self.addnewcus_page.set_admincomment("This is an Admin comment.")
        self.addnewcus_page.click_on_btn_save()

        self.list_email = self.addnewcus_page.assert_customer_email()

        self.msg = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]").text
        time.sleep(1)

        # act_title = self.driver.title
        # exp_title = "Customers / nopCommerce administration"
        # if act_title == exp_title:
        if self.msg == "×\nThe new customer has been added successfully.":
            if self.email == self.list_email:
                assert True
                self.driver.close()
                self.logger.info("****** Test Case 'test_add_new_customer' is Passed! ******")
            else:
                self.driver.save_screenshot(".\\Screenshots\\AddNewCustomer\\test_add_new_cus_email_assert.png")
                self.logger.error(f"User Emails didn't match! Before= {self.email}, After= {self.list_email}")
                self.driver.close()
                self.logger.error("****** Test Case 'test_add_new_customer' is Failed! ******")
                assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\AddNewCustomer\\test_add_new_cus_msg_assert.png")
            self.logger.error(f"Success Msg didn't match! {self.msg}")
            self.driver.close()
            self.logger.error("****** Test Case 'test_add_new_customer' is Failed! ******")
            assert False













