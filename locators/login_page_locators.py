from selenium.webdriver.common.by import By


class LoginPageLocators:

    RECOVER_PASSWORD = By.XPATH, './/*[text()="Восстановить пароль"]'
    RECOVER_BUTTON = By.XPATH, "//*[text()='Восстановить']"
    EMAIL = By.XPATH, "//input[@name ='name']"
    PASSWORD = By.XPATH, "//input[@name ='Пароль']"
    LOGIN_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    ENTER_NEW_PASSWORD = By.XPATH, ".//input[@name='Введите новый пароль']"
    SHOW_HIDE_BUTTON = By.CSS_SELECTOR, ".input__icon.input__icon-action"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"
    LOGIN_BUTTON_ACCOUNT = By.XPATH, '//*[@id="root"]/div/header/nav/a'
    ORDER_HISTORY = By.XPATH, "//*[text()='История заказов']"
    LOGOUT_BUTTON = By.XPATH, "//*[text()='Выход']"
    COVER_ELM = By.XPATH, './/div[@class="Modal_modal_overlay__x2ZCr"]'


