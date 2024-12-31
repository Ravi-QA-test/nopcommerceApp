# We can't directly read the data from 'config.ini' and provide them to our test case.
# So we created this 'readProperties.py' file, to read the common data which is stored in 'config.ini'.
# In other words, 'readProperties.py' file acts as an interpreter between 'config.ini' & the test case.
# This 'readProperties.py' is basically a utility file,
# which gets common data from 'config.ini' & then provide back the same data to the test case.

# For each variable, should create a respective method.

import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    # We need to access def getAppplicationURL(), method directly using classname 'ReadConfig'
    # In other words, without creating any instances of 'ReadConfig' class,
    # we need to access the class 'ReadConfig' directly.
    # Which means, we need to make the def getAppplicationURL() method, a static method.
    # So, we removed 'self' from def getAppplicationURL(self) method
    # and put @staticmethod, before def getAppplicationURL().

    @staticmethod
    def getAppplicationURL():
        url = config.get('Common Info','baseURL')
        return url

    @staticmethod
    def getUsername():
        email = config.get('Common Info', 'username' )
        return email

    @staticmethod
    def getPassword():
        password = config.get('Common Info', 'password')
        return password

