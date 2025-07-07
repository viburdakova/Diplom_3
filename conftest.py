import pytest
from selenium import webdriver

import data
from data import Payload, LOGIN_URL
from helpers.user_api import UserApi
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
def login_user(driver, create_user):
    _, data = create_user
    user_email = data["email"]
    user_password = data["password"]

    page = LoginPage(driver)
    page.go_to_url(LOGIN_URL)
    page.auth_personal_account(email=user_email, password=user_password)

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.go_to_url(data.LOGIN_URL)
    return page

@pytest.fixture
def create_user():
    data = Payload.generate_user_data()
    response, _ = UserApi.create_user(data)
    yield response, data
    UserApi.delete_user(response["accessToken"])

@pytest.fixture
def create_order(driver, login_user):
    page = MainPage(driver)
    page.go_to_constructor()
    page.add_ingredient_to_order()
    return page.place_order()

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
