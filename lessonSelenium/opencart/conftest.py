import pytest
import os

from selenium import webdriver
from datetime import datetime

DRIVERS = os.path.expanduser('~/webDrivers/')


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://demo.opencart.com/')


@pytest.fixture(scope='module')
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        service = webdriver.ChromeService(executable_path=f'{DRIVERS}chromedriver')
        driver = webdriver.Chrome(service=service)
    elif browser == 'ff' or 'firefox':
        service = None
        driver = webdriver.Firefox(service=service)
    elif browser == 'safari':
        driver = webdriver.Safari
    else:
        raise AttributeError(f'Browser param :: there is no {browser} driver')
    base_url = request.config.getoption('--url')
    if base_url:
        driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    failed_before = request.session.testsfailed

    def teardown():
        if request.session.testsfailed != failed_before:
            take_screenshot(driver, request)
        driver.quit()

    request.addfinalizer(teardown)
    return driver


def take_screenshot(driver, request):
    test_name = request.node.nodeid.split('::')[-1]
    time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'{test_name}__{time_now}.png'
    project_dir_path = os.path.dirname(__file__)
    screenshot_dir = os.path.realpath(os.path.join(project_dir_path, "screenshots", file_name))
    driver.save_screenshot(screenshot_dir)
