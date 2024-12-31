import pytest
import pytest_html
import undetected_chromedriver as uc
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
import undetected_geckodriver as ug
from undetected_geckodriver import Firefox

# Common things we introduce in the 'conftest.py' file
# This 'conftest.py' is applicable for all test cases.

#=================To Run Tests on Desired Browser====================
# To run this test on Chrome, open terminal and type;
# pytest -vs testCases/test_login.py --browser chrome

# To run this test on Firefox, open terminal and type;
# pytest -vs testCases/test_login.py --browser firefox

# To run this test on default browser (without specifying browser), open terminal and type;
# pytest -vs testCases/test_login.py
#---------------------------------------------------------------------------------------------

#===================To Run Tests Parallel======================
# pytest -vs -n=2 testCases/test_login.py

# Here, -n is denoted by number of methods we are going to run.
# -n=2 means, we are going to run 2 test methods.
#----------------------------------------------------------------------------------------------

#===========To Run Tests Parallel on Desired browser============
# pytest -vs -n=2 testCases/test_login.py --browser chrome
#----------------------------------------------------------------------------------------------

@pytest.fixture()
def setup(browser):

    try:
        # Initialize the WebDriver with Chrome class
        if browser == "chrome":
            options = uc.ChromeOptions()
            options.add_argument("--password-store=basic")
            options.add_experimental_option("prefs",
                {"credentials_enable_service": False, "profile.password_manager_enabled": False,},)
            driver = uc.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            print("No browser was specified. So running using default browser, chrome")
        return driver
    except BaseExceptionGroup as e:
        print("Error in Driver: ",e)

# This method will get the value from CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    # default = "chrome"
    # If browser name isn't specified when running the test case, then default browser will use to run the test.

# This method will return the browser value to the setup method
@pytest.fixture()
def browser(request):
    browser_name = (request.config.getoption("--browser"))
    return browser_name

#================Generate PyTest HTML Reports==================

def pytest_html_report_title(report):
    report.title = "NOP Commerce Test Report"

# # It's a hook for Adding Environment info/Customized info, to HTML Report
# def pytest_configure(config):
#     config._metadata = {
#             "Tester": "Dumedya",
#             "Python Version": "3.12.6",
#             "Platform": "Windows 11",
#             "Project Name": "nop commerce App",
#             "Module Name": "Customers"}

def pytest_configure(config):
    config.stash[metadata_key]["Tester"] = "Dumedya"
    config.stash[metadata_key]["Module Name"] = "Customers"

# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     session.config.stash[metadata_key]["Tester"] = "Dumedya"

# It's a hook to Delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)
# In here, I don't need default info like: JAVA HOME & Plugins, so I made it as 'None'.

# Below part is to Edit the 'Summary' section
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend(["<p>Tester: DR</p>"])


# To Run PyTest HTML Reports, use command;
# pytest -vs -n=2 --html=Reports/reportd.html testCases/test_login.py







