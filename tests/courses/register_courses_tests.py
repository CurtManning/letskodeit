from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.tststatus import TstStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):
    """
    py.test -v -s tests/courses/register_courses_tests.py --browser firefox
    py.test -v -s tests/courses/register_courses_tests.py --html=htmlreport.html

    Verify pytest is installed installed
    pip3 install pytest

    Make sure Install pytest-ordering and pytest in system terminal using the pip3 command.
    pip3 install pytest-ordering

    If pytest-html is not installed, from the terminal type : pip3 install pytest-html

    """

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver, self.cfg, self.bitConfig)
        self.ts = TstStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1234 5678 9012 3456", exp="1220", cvv="444", zip="12345")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")