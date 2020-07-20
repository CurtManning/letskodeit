from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.tststatus import TstStatus
from utilities.read_data import getCSVData
import unittest, pytest
from ddt import ddt, data, unpack
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):
    """
    

    To run html reports verify pytest-html is installed. If is not installed, from the terminal type : pip3 install pytest-html

    """
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver, self.cfg)
        self.ts = TstStatus(self.driver)
        self.nav = NavigationPage(self.driver, self.cfg)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, ccZip):
        self.courses.enterCourseName(courseName)
        time.sleep(1)
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=ccZip)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.driver.back()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")