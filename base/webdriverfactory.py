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
        # Put your username and authey below
        # You can find your authkey at crossbrowsertesting.com/account
        self.username = "curtmanning@ltgc.com"
        self.authkey = "ucc45ee689bfd25a"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username, self.authkey)


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
        # start the remote browser on our server
        caps = {}

        caps['name'] = 'Login Form Example'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['version'] = '72'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'
        caps['record_video'] = 'true'
        caps['record_network'] = 'false'

        driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
