import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from PageObject.DriveHomePage import GoogleDrivePage
from PageObject.DriveLogin import LoginPage
from PageObject.GoogleDoc import DocHomePage


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass
