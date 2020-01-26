from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    """
    Make sure Install pytest-ordering and pytest in system terminal using the pip command.

    py.test -v -s tests/home/login_tests.py --browser firefox
    py.test -v -s tests/home/login_tests.py --browser chrome

    """

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        assert result1 == True
        result2 = self.lp.verifyLoginSuccessful()
        assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
