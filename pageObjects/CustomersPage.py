from selenium.webdriver.common.by import By
import time

class CustomersPage:

    lnk_customers_menu_xpath = "//p[contains(.,'Customers')]"
    lnk_customers_menuitem_xpath = "//li[4]/ul/li/a/p"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menu_xpath).click()
        time.sleep(3)

    def click_on_customers_menuitem(self):
        self.driver.find_element(By.XPATH, self.lnk_customers_menuitem_xpath).click()
        time.sleep(4)

# (1) Why we use Page Object Model (POM)?
# Ans: Once we locate the elements, we can reuse those elements in multiple test cases using POM.
# We don't run the page object class. (Ex: LoginPage.py)
# We only run the test class. (Ex: test_login.py)
