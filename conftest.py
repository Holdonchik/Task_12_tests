import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )
    parser.addoption(
        "--driver_folder", default=os.path.expanduser("~/drivers")
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--url", default="https://www.opencart.ru/"
    )


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")
    driver = None

    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        options.headless = headless
        options.binary_location = "C:/Users/Admin/AppData/Local/Mozilla Firefox/firefox.exe"
        driver = webdriver.Firefox(executable_path=f"{driver_folder}{os.sep}geckodriver", options=options)

    elif _browser == "chrome":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(executable_path=f"{driver_folder}{os.sep}chromedriver", options=options)
    else:
        raise Exception("Driver not supported")

    driver.url = url
    driver.maximize_window()
    # driver.implicitly_wait(20)

    yield driver
    driver.close()

