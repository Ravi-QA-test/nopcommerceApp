from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerate
from utilities import ExcelUtils
import pytest
import time

class TestLogin_DDT_002:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getAppplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGenerate.loggen()

    # @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("********** test_login_ddt **********")
        # Replaced, driver = webdriver.Chrome() with, self.driver = setup, as below.
        self.driver = setup  # 'driver' object returned from "conftest.py' stores here.
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)
        self.login_page = LoginPage(self.driver)

        self.rows = ExcelUtils.get_row_count(self.path, "Sheet1")
        self.read_data = ExcelUtils.read_data(self.path, "Sheet1", 1, 2)
        print("Number of Raws in the Excel:", self.rows)
        print("")
        # print("Data in the 2nd Column of Excel:", self.read_data)

        list_status = []       # Empty List variable 'list_status' created to store Expected results

        # Below, for loop will read data from the Excel file.
        # r = Rows
        # range(range start, range end)
        # Inside the range(); since the first raw being the header part, we started the range from 2.
        # range(2, )
        # Inside the range(); self.rows won't take the last raw bydefault. So we need to add 1 to self.rows.
        # range(2, self.rows+1)
        for r in range(2,self.rows+1):
            self.username = ExcelUtils.read_data(self.path,"Sheet1", r,1)  # username column
            self.password = ExcelUtils.read_data(self.path, "Sheet1", r, 2) # password column
            self.expected = ExcelUtils.read_data(self.path, "Sheet1", r, 3) # expected column
            print("Data in Username column", self.username)
            print("Data in Password column", self.password)
            print("Data in Expected column", self.expected)
            print("")

            # Below, 2 methods will pass data to our application.
            self.login_page.set_username(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expected == "Pass":  #Act title matched Exp title & in Excel sheet result is also 'Pass'
                    time.sleep(2)
                    self.logger.info("*** Passed! ***")
                    self.login_page.click_logout()
                    list_status.append("Pass")    # Update the list with result 'Pass'
                    self.logger.info("Status Added to the list")
                elif self.expected == "Fail": #Act title matched Exp title but in Excel sheet result is 'Fail'
                    time.sleep(2)
                    self.logger.error("*** Failed! ***")
                    self.login_page.click_logout()
                    list_status.append("Fail")
                    self.logger.info("Status Added to the list")
            elif act_title != exp_title:
                if self.expected == "Pass": #Act title didn't match Exp title but in Excel sheet result is 'Pass'
                    time.sleep(2)
                    self.logger.info("*** Failed! ***")
                    list_status.append("Fail")
                    self.logger.info("Status Added to the list")
            elif self.expected == "Fail": #Act title didn't match Exp title & also in Excel sheet result is 'Fail'
                time.sleep(2)
                self.logger.info("*** Passed! ***")
                list_status.append("Pass")
                self.logger.info("Status Added to the list")

        if "Fail" not in list_status:
            self.logger.info("***** Test Case 'test_login_ddt' is Passed! *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Test Case 'test_login_ddt' is Failed! *****")
            self.driver.close()
            assert False

        self.logger.info("******* End of 'test_login_ddt' *******")
        self.logger.info("******* Completed Test Case 'TestLogin_DDT_002' *******")











