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
        self.bitConfig = bitConfig
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

        if self.config.prod(self.bitConfig):
            self.log.info("Bit Config = Prod")
            print("Bit Config = Prod")
            baseUrl = "https://letskodeit.teachable.com/"
        elif self.config.staging(self.bitConfig):
            self.log.info("Bit Config = Staging")
            print("Bit Config = Staging")
            baseUrl = "https://letskodeit.teachable.com/"
        else:
            print("Bit Config = OTHER")
            self.log.info("Bit Config = OTHER")
            baseUrl = "https://letskodeit.teachable.com/"

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\Users\\curtmanning\\selenium\\geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "C:\\Users\\curtmanning\\selenium\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            #driver.set_window_size(1440, 900)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
