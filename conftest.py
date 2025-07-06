import pytest
from selenium import webdriver

import data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(data.LOGIN_URL)
    return page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(data.MAIN_URL)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(data.FEED_URL)
    return page
