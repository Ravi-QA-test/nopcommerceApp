from selenium.webdriver.common.by import By
import time

class OnlineCustomersPage:

     lnk_onlinecustomers_menuitem_xpath = "//li[4]/ul/li[3]/a/p"

     def __init__(self, driver):
         self.driver = driver

     def click_on_onlinecustomers_menu(self):
         self.driver.find_element(By.XPATH, self.lnk_onlinecustomers_menuitem_xpath).click()
         time.sleep(3)