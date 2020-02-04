import utilities.custom_logger as cl
import logging
from configparser import ConfigParser
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):
    """
    pip3 install pytest-ordering

    py.test -v -s tests/courses/register_courses_tests.py --browser firefox

    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, cfg):
        super().__init__(driver)
        self.driver = driver
        self.cfg = cfg

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        locator = self.cfg.get("locators", "search_box")
        print(" Locator = " + locator)
        # self.clearField(self.cfg.get("locators", "search_box"))
        self.sendKeys(name, locator=locator)
        locator1 = self.cfg.get("locators", "search_course_icon")
        print(" Locator1 = " + locator1)
        self.elementClick(locator=locator1)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self.cfg.get("locators", "course").format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(  locator=self.cfg.get("locators", "enroll_button"))

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame5")
        self.sendKeys(num, locator=self.cfg.get("locators", "cc_num"), locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame6")
        self.sendKeys(exp,  locator=self.cfg.get("locators", "cc_exp"), locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(name="__privateStripeFrame7")
        self.sendKeys(cvv, locator=self.cfg.get("locators", "cc_cvv"), locatorType="name")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        self.switchToFrame(name="__privateStripeFrame8")
        self.sendKeys(zip, locator=self.cfg.get("locators", "zip"), locatorType="name")
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self.cfg.get("locators", "agree_to_terms_checkbox"))

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self.cfg.get("locators", "submit_enroll"), locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, zip)
        self.clickAgreeToTermsCheckbox()

    def verifyEnrollFailed(self):
        """
        verify enroll failed
        
        :return:
        """
        result = self.isEnabled(locator=self.cfg.get("locators", "submit_enroll"), locatorType="xpath",
                                info="Enroll Button")
        return not result