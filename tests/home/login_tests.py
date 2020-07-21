from pages.home.login_page import LoginPage
from utilities.tststatus import TstStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    """

    Make sure Install pytest-ordering and pytest in system terminal using the pip command.
    pip install requests
    py.test -v -s tests/home/login_tests.py --browser firefox
    py.test -v -s tests/home/login_tests.py --browser chrome

    """

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TstStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        try:
            self.lp.login()
            result1 = self.lp.verifyLoginTitle()
            self.ts.mark(result1, "Title Verification")
            result2 = self.lp.verifyLoginSuccessful()
            self.ts.markFinal("test_validLogin", result2, "Login Verification")
            print("Taking snapshot")
            snapshot_hash1 = self.api_session.post(
                'https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id +
                '/snapshots').json()['hash']

            # if we are still in the try block after all of our assertions that
            # means our test has had no failures, so we set the status to "pass"
            self.test_result = 'pass'

        except AssertionError as e:
            # log the error message, and set the score to "during tearDown()".
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id +
                                 '/snapshots/' + snapshot_hash1, data={'description':"AssertionError: " + str(e)})
            self.test_result = 'fail'
            raise

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        try:
            self.lp.logout()
            self.lp.login("test@email.com", "abcabcabc")
            result = self.lp.verifyLoginFailed()
            assert result == True
            print("Taking snapshot")
            snapshot_hash = self.api_session.post(
                'https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id +
                '/snapshots').json()['hash']

            # if we are still in the try block after all of our assertions that
            # means our test has had no failures, so we set the status to "pass"
            self.test_result = 'pass'

        except AssertionError as e:
            # log the error message, and set the score to "during tearDown()".
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id +
                                 '/snapshots/' + snapshot_hash, data={'description':"AssertionError: " + str(e)})
            self.test_result = 'fail'
            raise
