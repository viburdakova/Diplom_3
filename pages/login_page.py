from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step("Перейти на страницу восстановления пароля в chrome")
    def go_to_password_recovery(self):
        self.click_on_element_firefox(LoginPageLocators.RECOVER_PASSWORD)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/forgot-password"))

    @allure.step("Ввести email и кликнуть на кнопку восстановить в chrome")
    def submit_password_recovery_form_chrome(self, login_data):
        self.add_text_element(LoginPageLocators.EMAIL, login_data['email'])
        self.click_to_element(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Ввести email и кликнуть на кнопку восстановить в firefox ")
    def submit_password_recovery_form_firefox(self, login_data):
        self.add_text_element(LoginPageLocators.EMAIL, login_data['email'])
        self.click_on_element_firefox(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Ввести email и кликнуть на кнопку восстановить")
    def submit_password_recovery_form(self, login_data):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.submit_password_recovery_form_firefox(login_data)
        else:
            self.submit_password_recovery_form_chrome(login_data)

    @allure.step("Клик на личный кабинет в firefox")
    def click_personal_account(self):
        self.check_displaying_of_element(LoginPageLocators.LOGIN_BUTTON_ACCOUNT)
        self.click_on_element_firefox(LoginPageLocators.LOGIN_BUTTON_ACCOUNT)
        WebDriverWait(self.driver, 20).until(EC.url_contains("account/profile"))

    def wait_until_cover_disappears(self):
        self.cover_elm_with_wait(LoginPageLocators.COVER_ELM)

    @allure.step("Авторизоваться в личном кабинете в chrome")
    def auth_personal_account_chrome(self, log_pass_data):
        self.add_text_element(LoginPageLocators.EMAIL, log_pass_data ['my_email'])
        self.add_text_element(LoginPageLocators.PASSWORD, log_pass_data['my_password'])
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизоваться в личном кабинете в firefox")
    def auth_personal_account_firefox(self, log_pass_data):
        self.add_text_element(LoginPageLocators.EMAIL, log_pass_data['my_email'])
        self.add_text_element(LoginPageLocators.PASSWORD, log_pass_data['my_password'])
        self.click_on_element_firefox(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизоваться в личном кабинете")
    def auth_personal_account(self, logo_pass_data):
        browser_name = self.driver.name
        if browser_name == 'firefox':
            self.auth_personal_account_firefox(logo_pass_data)
        else:
            self.auth_personal_account_chrome(logo_pass_data)

    @allure.step("Перейти в личный кабинет в chrome")
    def go_to_personal_account_chrome(self):
        self.click_to_element(LoginPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/account/profile"))

    @allure.step("Перейти в личный кабинет в firefox")
    def go_to_personal_account_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/account/profile"))

    @allure.step("Перейти в личный кабинет")
    def click_personal_account(self):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.go_to_personal_account_firefox()
        else:
            self.go_to_personal_account_chrome()

    @allure.step("Перейти в историю заказов в chrome")
    def go_to_order_history_chrome(self):
        self.click_to_element(LoginPageLocators.ORDER_HISTORY)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/account/order-history"))

    @allure.step("Перейти в историю заказов в firefox")
    def go_to_order_history_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.ORDER_HISTORY)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/account/order-history"))

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.go_to_order_history_firefox()
        else:
            self.go_to_order_history_chrome()

    @allure.step("Выйти из аккаунта в chrome")
    def logout_chrome(self):
        self.click_to_element(LoginPageLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/login"))

    @allure.step("Выйти из аккаунта в firefox")
    def logout_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/login"))

    @allure.step("Выйти из аккаунта")
    def logout(self):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.logout_firefox()
        else:
            self.logout_chrome()

    @allure.step("Проверить что пользователь авторизован")
    def is_authorized(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
            return True
        except:
            return False

    @allure.step("Проверка подсвечивания поля пароль при клике на кнопку скрыть/показать")
    def is_password_field_highlighted(self):
        self.click_on_element_firefox(LoginPageLocators.SHOW_HIDE_BUTTON)
        try:
            WebDriverWait(self.driver, 20).until(
                lambda d: 'input_status_active' in
                            d.find_element(*LoginPageLocators.ENTER_NEW_PASSWORD).get_attribute('class')
                )
            return True
        except:
            return False