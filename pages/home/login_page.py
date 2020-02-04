import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, cfg):
        super().__init__(driver)
        self.driver = driver
        self.cfg = cfg
        self.nav = NavigationPage(driver, cfg)

        self.user_id = self.cfg.get("credentials", "user_id")
        self.user_password = self.cfg.get("credentials", "user_password")

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self):
        self.sendKeys(self.user_id, self._email_field)

    def enterPassword(self):
        self.sendKeys(self.user_password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self):
        self.clickLoginLink()
        self.enterEmail()
        self.enterPassword()
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@id='navbar']//li[@class='dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)