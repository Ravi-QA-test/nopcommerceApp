import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = uc.ChromeOptions()
options.add_argument("--password-store=basic")
options.add_experimental_option("prefs",
                                {"credentials_enable_service": False, "profile.password_manager_enabled": False, }, )
driver = uc.Chrome(options=options)
driver.maximize_window()
driver.get("https://admin-demo.nopcommerce.com/")
time.sleep(2)
driver.find_element(By.ID, "Email").clear()
time.sleep(1)
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
time.sleep(1)
driver.find_element(By.ID, "Password").clear()
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("admin")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//p[contains(.,'Customers')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[4]/ul/li/a/p").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Add new").click()
time.sleep(2)
driver.find_element(By.ID, "Email").send_keys("xdm@gmail.com")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("Ravi123#")
time.sleep(1)
driver.find_element(By.ID, "FirstName").send_keys("Ravindu")
time.sleep(1)
driver.find_element(By.ID, "LastName").send_keys("Perera")
time.sleep(1)
driver.find_element(By.ID, "Gender_Male").click()
time.sleep(1)
driver.find_element(By.ID, "DateOfBirth").click()
time.sleep(1)
driver.find_element(By.ID, "DateOfBirth").send_keys("09/01/1996")
time.sleep(1)
driver.find_element(By.ID, "Company").send_keys("IFS")
time.sleep(1)
driver.find_element(By.ID, "IsTaxExempt").click()
time.sleep(1)
Select(driver.find_element(By.NAME, "SelectedNewsletterSubscriptionStoreIds")).select_by_visible_text("Test Store 2")
time.sleep(1)
# newsletter.select_by_visible_text("Test store 2")
# time.sleep(1)
Select(driver.find_element(By.NAME, "SelectedCustomerRoleIds")).select_by_visible_text("Guests")
time.sleep(1)
# customer_roles.select_by_visible_text("Guests")
# time.sleep(1)
# driver.find_element(By.XPATH, "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[2]").click()
# time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='VendorId']/option[2]").click()
time.sleep(1)
driver.find_element(By.ID, "AdminComment").click()
time.sleep(1)
driver.find_element(By.ID, "AdminComment").send_keys("This is an admin comment!")
time.sleep(1)
driver.find_element(By.NAME, "save").click()
time.sleep(1)

driver.quit()












