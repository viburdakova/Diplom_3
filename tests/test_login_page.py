import allure
import pytest
import data
from conftest import driver, login_page

class TestLogin:

    @allure.feature("Восстановление пароля")
    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Проверка перехода на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_password_recovery(self, driver, login_page):
        login_page.go_to_password_recovery()
        login_page.submit_password_recovery_form(data.login_data)
        assert login_page.is_password_field_highlighted()

    @allure.feature("Личный кабинет")
    @allure.title("Переход на страницу личного кабинета")
    @allure.description("Проверка  перехода на страницу 'Личный кабинет', 'История заказов', logout")
    def test_personal_account_navigation(self, driver, login_page):
        login_page.wait_until_cover_disappears()
        login_page.auth_personal_account(data.log_pass_data)
        login_page.wait_until_cover_disappears()
        login_page.click_personal_account()
        login_page.go_to_order_history()
        login_page.logout()
        assert not login_page.is_authorized()
