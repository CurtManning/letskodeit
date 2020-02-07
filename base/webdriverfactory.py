"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import traceback
from selenium import webdriver
from utilities.bit_config import Config
import utilities.custom_logger as cl
import logging

class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser, cfg, bitConfig):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.cfg = cfg
        self.bitConfig = int(bitConfig)
        self.config = Config()
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        print('getWebDriverInstance -> Sections in the file:', self.cfg.sections())
        print('getWebDriverInstance -> BitConfig:', str(self.bitConfig))
        driverPath = os.path.abspath(".\\driver") + "\\"

        if self.config.prod(self.bitConfig):
            self.log.info("getWebDriverInstance -> Bit Config = Prod")
            print("getWebDriverInstance - Bit Config = Prod")
            baseUrl = "https://letskodeit.teachable.com/"

        elif self.config.staging(self.bitConfig):
            self.log.info("getWebDriverInstance -> Bit Config = Staging")
            print("getWebDriverInstance -> Bit Config = Staging")
            baseUrl = "https://letskodeit.teachable.com/"

        else:
            print("getWebDriverInstance - Bit Config = OTHER")
            self.log.info("getWebDriverInstance -> Bit Config = OTHER")
            baseUrl = "https://letskodeit.teachable.com/"

        if self.browser == "iexplorer" or self.config.edge(self.bitConfig):
            # Set ie driver
            self.log.info("getWebDriverInstance - Set ie driver")
            driverLocation = driverPath + "IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            driver = webdriver.Ie(driverLocation)

        elif self.browser == "firefox" or self.config.firefox(self.bitConfig):
            # Set firefox driver
            self.log.info("Set firefox driver")
            executable = driverPath + "geckodriver.exe"
            driver = webdriver.Firefox(executable_path=executable)

        elif self.browser == "chrome" or self.config.chrome(self.bitConfig):
            # Set chrome driver
            self.log.info("Set chrome driver")
            executable = driverPath + "chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = executable
            driver = webdriver.Chrome(executable)

        else:
            self.log.info("Set default to firefox driver")
            executable = driverPath + "geckodriver.exe"
            driver = webdriver.Firefox(executable_path=executable)

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
