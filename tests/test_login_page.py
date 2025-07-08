import allure
import data
from conftest import driver, login_page, login_user, create_user

class TestLogin:

    @allure.feature("Восстановление пароля")
    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Проверка перехода на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_password_recovery(self, login_page):
        login_page.go_to_password_recovery()
        login_page.submit_password_recovery_form(data.login_data)
        login_page.click_show_hide_button()
        assert login_page.check_is_password_is_active

    @allure.feature("Личный кабинет")
    @allure.title("Переход на страницу личного кабинета")
    @allure.description("Проверка  перехода на страницу 'Личный кабинет', 'История заказов', logout")
    def test_personal_account_navigation(self, login_page, login_user):
        login_page.click_personal_account()
        login_page.go_to_order_history()
        login_page.logout()
        assert not login_page.is_authorized()
