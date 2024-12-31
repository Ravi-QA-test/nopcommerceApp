from selenium.webdriver.common.by import By
import time

class SearchCustomerPage:

    txt_search_email_id = "SearchEmail"
    txt_search_firstname_id = "SearchFirstName"
    txt_search_lastname_id = "SearchLastName"
    btn_search_id = "search-customers"
    fname_table_xpath = "//*[@id='customers-grid']/tbody/tr/td[3]"
    arrow_down_xpath = "//i[@class='far fa-angle-down']"

    def __init__(self, driver):
        self.driver = driver

    def click_downwards_arrow(self):
        self.driver.find_element(By.XPATH, self.arrow_down_xpath).click()
        time.sleep(1)

    def set_search_email(self, email):
        self.driver.find_element(By.ID, self.txt_search_email_id).send_keys(email)
        time.sleep(1)

    def set_search_firstname(self, firstname):
        self.driver.find_element(By.ID, self.txt_search_firstname_id).send_keys(firstname)
        time.sleep(1)

    def set_search_lastname(self, lastname):
        self.driver.find_element(By.ID, self.txt_search_lastname_id).send_keys(lastname)
        time.sleep(1)

    def click_on_search(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()
        time.sleep(3)

    def search_cus_by_firstname(self):
        # Since we require to find multiple elements,
        # We've used 'find_elements' below, not the 'find_element'.
        name_elements = self.driver.find_elements(By.XPATH, self.fname_table_xpath)
        texts = [element.text for element in name_elements]
        return texts

