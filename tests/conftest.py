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
def oneTimeSetUp(request, browser, bitConfig):
    print("Running one time setUp")
    config_num = int(bitConfig)
    cfg = ConfigParser()
    cfg.read('config.ini')
    print("Sections in the file:" + str(cfg.sections()))
    print("BitConfig:" + str(config_num))
    # print('Sections in the file:', str(config))
    wdf = WebDriverFactory(browser, cfg, config_num)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver, cfg)
    lp.login()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.cfg = cfg
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--bitConfig", help="Bit Configuration")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def bitConfig(request):
    return request.config.getoption("--bitConfig")