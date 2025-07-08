

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_on_element_firefox(MainPageLocators.CONSTRUCTOR)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER))

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_on_element_firefox(MainPageLocators.ORDER_FEED_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ORDER_FEED))

    @allure.step("Открыть детали ингредиента")
    def open_ingredient_details(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        ingredient.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.MODAL_WINDOW)
        )

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        ).click()

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        WebDriverWait(self.driver, 20).until_not(
            EC.text_to_be_present_in_element(MainPageLocators.ORDER_ID, '9999')
        )
        order_num = self.get_text(MainPageLocators.ORDER_ID)

        return order_num

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        try:
            counter = self.find_element(MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        constructor = self.find_element(MainPageLocators.BURGER_CONSTRUCTOR)

        if self.driver.name == 'firefox':
            self.drag_and_drop_element_firefox(ingredient, constructor)
        else:
            ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()

        WebDriverWait(self.driver, 10).until(
            lambda d: self.get_ingredient_counter() > 0
        )

    @allure.step("Оформить заказ (для авторизованного пользователя)")
    def place_order(self):
        self.find_element(MainPageLocators.PLACE_AN_ORDER).click()
        self.wait_for_clickable(OrderPageLocators.ORDER_MODAL)
        self.wait_for_invisibility(OrderPageLocators.DEFAULT_ORDER_NUMBER)
        self.wait_for_visible(OrderPageLocators.ORDER_TEXT)
        order_number = self.wait_for_clickable(OrderPageLocators.ACTUAL_ORDER_NUMBER).text
        self.get_click(OrderPageLocators.CLOSE_MODAL_BUTTON)
        return order_number
