# This is the Page Object Class for Login screen.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage:

    txt_username_id = "Email"
    txt_password_id = "Password"
    btn_login_xpath = "//button[@type='submit']"
    lnk_logout_linktext = "Logout"
    # Now we've identified all the locators

    # Initialized the driver, using the constructor
    def __init__(self, driver):
        self.driver = driver

    # Now implemented actions/methods for each locator
    def set_username(self, username):
        self.driver.find_element(By.ID, self.txt_username_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self.txt_username_id).send_keys(username)
        time.sleep(1)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        time.sleep(2)
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
        time.sleep(1)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        time.sleep(6)

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_logout_linktext).click()
        time.sleep(4)


