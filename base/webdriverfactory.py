"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
        driverLocation = "/home/runner/work/qa_test_tutorial/qa_test_tutorial/drivers/linux/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation

        options = Options()
        options.add_argument("--no-sandbox")  # bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        options.add_argument("--headless")  # overcome limited resource problems
        driver = webdriver.Chrome(options=options, executable_path=driverLocation)

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        baseUrl = "https://letskodeit.teachable.com/"
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
