from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):
    """
    py.test -v -s tests/home/login_tests.py

    """

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox(executable_path="C:\\Users\\CurtA\\selenium\\geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        driver.quit()