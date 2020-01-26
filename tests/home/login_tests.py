from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

class LoginTests(unittest.TestCase):
    """
    Make sure Install pytest-ordering and pytest in system terminal using the pip command.

    py.test -v -s tests/home/login_tests.py

    """
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Firefox(executable_path="C:\\Users\\CurtA\\selenium\\geckodriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.clearLoginFields()
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True