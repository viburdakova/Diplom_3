from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    @allure.step("Перейти на страницу восстановления пароля в chrome")
    def go_to_password_recovery(self):
        self.get_click(LoginPageLocators.RECOVER_PASSWORD)
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.FORGOT_PASSWORD))

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

    @allure.step("Клик на личный кабинет")
    def click_personal_account(self):
        self.get_click(LoginPageLocators.LOGIN_BUTTON_ACCOUNT)
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.PROFILE_URL))

    def wait_until_cover_disappears(self):
        self.cover_elm_with_wait(LoginPageLocators.COVER_ELM)

    @allure.step("Авторизоваться в личном кабинете")
    def auth_personal_account(self, email, password):
        self.add_text_element(LoginPageLocators.EMAIL, email)
        self.add_text_element(LoginPageLocators.PASSWORD, password)
        self.get_click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_invisibility(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Перейти в личный кабинет в chrome")
    def go_to_personal_account_chrome(self):
        self.click_to_element(LoginPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(EC.url_contains(data.PROFILE_URL))

    @allure.step("Перейти в личный кабинет в firefox")
    def go_to_personal_account_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(EC.url_contains(data.PROFILE_URL))

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
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.ORDER_HISTORY))

    @allure.step("Перейти в историю заказов в firefox")
    def go_to_order_history_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.ORDER_HISTORY)
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.ORDER_HISTORY))

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
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.LOGIN_URL))

    @allure.step("Выйти из аккаунта в firefox")
    def logout_firefox(self):
        self.click_on_element_firefox(LoginPageLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains(data.LOGIN_URL))

    @allure.step("Выйти из аккаунта")
    def logout(self):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.logout_firefox()
        else:
            self.logout_chrome()

    @allure.step("Клик на кнопку показть/скрыть пароль")
    def click_show_hide_button(self):
        self.click_on_element_firefox(LoginPageLocators.SHOW_HIDE_BUTTON)

    @allure.step("Проверка, что поле пароля активно")
    def check_is_password_is_active(self):
        return self.check_displaying_of_element(LoginPageLocators.PASSWORD_IS_ACTIVE)

    @allure.step("Проверить что пользователь авторизован")
    def is_authorized(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginPageLocators.LOGOUT_BUTTON))
            return True
        except:
            return False