from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.customLogger import LogGenerate
import random
import string
import time

class AddNewCustomerPage:

    lnk_addnewcustomer_linktext = "Add new"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstname_id = "FirstName"
    txt_lastname_id = "LastName"
    rdbtn_gender_id = "Gender_Male"
    datepkr_dob_id = "DateOfBirth"       # datepkr_dob_xpath = "//input[@id='DateOfBirth']"
    txt_companyname_id = "Company"
    chkbox_taxexempt_id = "IsTaxExempt"
    multidrpdwn_newsletter_xpath = "SelectedNewsletterSubscriptionStoreIds"
    lstbox_customerroles_xpath = "SelectedCustomerRoleIds"
    drpdwn_vendor_xpath = "//*[@id='VendorId']/option[2]"
    txt_admincomment_id = "AdminCommen"
    btn_save_name = "save"
    mail_grid_xpath = "//*[@id='customers-grid']/tbody/tr[1]/td[2]"

    # Initialized the driver, using the constructor
    def __init__(self, driver):
        self.driver = driver

    # def take_screenshot(self, method_name):
    #     self.driver.save_screenshot(f".\\Screenshots\\{method_name}.png")

    logger = LogGenerate.loggen()

        # We use 'self' keyword to access all variables belongs to the Class.
        # These methods should be called in 'test_add_new_cutomer' and not in here.
        # So commenting these 3 methods.
        # self.customer_page = CustomersPage(self.driver)
        # self.customer_page.click_on_customers_menu()
        # self.customer_page.click_on_customers_menuitem()

    # Now implemented actions for each locator

    def click_on_add_new_customer(self):
        self.driver.find_element(By.LINK_TEXT, self.lnk_addnewcustomer_linktext).click()
        time.sleep(2)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)
        time.sleep(1)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)
        time.sleep(1)

    def set_firstname(self, firstname):
        self.driver.find_element(By.ID, self.txt_firstname_id).send_keys(firstname)
        time.sleep(1)

    def set_lastname(self, lastname):
        self.driver.find_element(By.ID, self.txt_lastname_id).send_keys(lastname)
        time.sleep(1)

    def select_gender(self):
        self.driver.find_element(By.ID, self.rdbtn_gender_id).click()
        time.sleep(1)

    def select_dob(self, dob):
        # self.driver.find_element(By.ID, self.datepkr_dob_id).click()
        # time.sleep(1)
        # "09/01/1996"
        self.driver.find_element(By.ID, self.datepkr_dob_id).send_keys(dob)
        time.sleep(1)

    def set_company(self, company):
        self.driver.find_element(By.ID, self.txt_companyname_id).send_keys(company)
        time.sleep(1)

    def click_on_istaxexempt(self):
        self.driver.find_element(By.ID, self.chkbox_taxexempt_id).click()
        time.sleep(1)

    def select_newsletter(self, newsletter):
        # "Test store 2"
        Select(self.driver.find_element(By.NAME, self.multidrpdwn_newsletter_xpath)).select_by_visible_text(
            newsletter)
        time.sleep(1)

    def select_customer_roles(self, role):
        # "Vendors"
        Select(self.driver.find_element(By.NAME, self.lstbox_customerroles_xpath)).select_by_visible_text(role)
        time.sleep(1)

    def select_vendor(self):
        self.driver.find_element(By.XPATH, self.drpdwn_vendor_xpath).click()
        time.sleep(1)

    def set_admincomment(self, comment):
        self.driver.find_element(By.ID, self.txt_admincomment_id).send_keys(comment)
        time.sleep(1)
        # try:
        #     self.driver.find_element(By.ID, self.txt_admincomment_id).send_keys(comment)
        #     time.sleep(1)
        # except Exception as e:
        #     # self.take_screenshot("set_admincomment")
        #     self.driver.save_screenshot(".\\Screenshots\\AddNewCustomer\\set_admincomment.png")
        #     self.logger.error(e)

    def click_on_btn_save(self):
        self.driver.find_element(By.NAME, self.btn_save_name).click()
        time.sleep(2)


# ==================================================================================
        # try:
        #     self.driver.find_element(By.NAME, self.btn_save_name).click()
        # except Exception as e:
        #     self.driver.save_screenshot('screenshot.png')
# ===================================================================================
        # import time
        #
        # def click_on_btn_save(self):
        #     try:
        #         self.driver.find_element(By.NAME, self.btn_save_name).click()
        #     except Exception as e:
        #         timestamp = time.strftime("%Y%m%d-%H%M%S")
        #         screenshot_name = f"screenshot_{timestamp}.png"
        #         self.driver.save_screenshot(screenshot_name)
# ====================================================================================


    @staticmethod
    def generate_random_email():
        domain = "@gmail.com"
        username_length = random.randint(5, 7)
        username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(username_length))
        return username + domain

    # Example usage
    # random_email = generate_random_email()
    # print(random_email)

    def assert_customer_email(self):
        grid_mail = self.driver.find_element(By.XPATH, self.mail_grid_xpath).text
        return grid_mail



