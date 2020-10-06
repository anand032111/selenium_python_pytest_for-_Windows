import time

import pytest
from selenium import webdriver
from PageObject.DriveLogin import LoginPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/Dell/Downloads/chromedriver_win32/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Ie(executable_path="/Users/nagarajualapati/PycharmProjects/Google_Pytest_e2e/driver"
                                              "/msedgedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://drive.google.com")
    print(driver.title)
    driver.find_element_by_xpath("//header//div[3]//div[1]//a[1]").click()
    driver.switch_to.window(driver.window_handles[1])
    login = LoginPage(driver)
    login.enter_username("testuser30071")
    login.click_on_next_button()
    login.enter_password("Test@3007")
    login.click_on_pwd_next_button()
    time.sleep(2)
    request.cls.driver = driver
    yield
    driver.quit()





@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".jpg"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
