import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from configparser import ConfigParser

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    cfg = ConfigParser()
    cfg.read('courses.ini')
    print('Sections in the file:', cfg.sections())
    # print('Sections in the file:', str(config))
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login(cfg.get("credentials", "user_id"), cfg.get("credentials", "user_password"))

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")