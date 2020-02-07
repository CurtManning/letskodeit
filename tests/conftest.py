import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage
from configparser import ConfigParser
from utilities.bit_config import Config
import os

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, bitConfig):
    """
    One Time Set Up

    :param request:
    :param browser:
    :return:
    """
    print("Running one time setUp")
    cfg = ConfigParser()
    bitcfg = Config()
    cfg.read(os.path.abspath(".\\configfiles\\config.ini"))

    if not bitConfig:
        bitConfig = str(bitcfg.configBuilder())

    wdf = WebDriverFactory(browser, cfg, bitConfig)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver, cfg)
    lp.login()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.cfg = cfg
        request.cls.bitConfig = bitConfig
    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--bitConfig", help="Integer(bit) Configuration")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def bitConfig(request):
    return request.config.getoption("--bitConfig")