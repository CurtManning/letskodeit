import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, cfg):
        super().__init__(driver)
        self.driver = driver
        self.cfg = cfg

    # Locators
    _my_courses = "//a[contains(text(),'My Courses')]"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _practice = "//a[contains(text(),'Practice')]"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigateToAllCourses(self):
        time.sleep(3)
        self.elementClick(locator=self._all_courses, locatorType="xpath")
        time.sleep(3)

    def navigateToMyCourses(self):
        self.waitForElement(locator=self._my_courses,
                            locatorType="xpath", pollFrequency=1)
        self.elementClick(locator=self._my_courses, locatorType="xpath")
        time.sleep(3)

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="xpath")
        time.sleep(3)

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
