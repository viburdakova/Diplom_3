import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def go_to_constructor(self):
        self.click_on_element_firefox(MainPageLocators.CONSTRUCTOR)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ASSEMBLE_BURGER))

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
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
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        ).click()

    @allure.step("Перетаскивание ингредиентов")
    def drag_and_drop(self, locator_from, locator_to):
        element_from = self.find_element(locator_from)
        element_to = self.find_elememt(locator_to)

        self.driver.drag_and_drop(element_from, element_to).perfom()

    @allure.step("Перетаскивание ингредиентов в firefox")
    def drag_and_drop_element_firefox(self, source_element, target_element):
        script = """
                function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                    var dataTransfer = new DataTransfer();
                    var dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragStartEvent);

                    var dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    destinationNode.dispatchEvent(dropEvent);
    				var dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    sourceNode.dispatchEvent(dragEndEvent);
                }
                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                """
        self.driver.execute_script(script, source_element, target_element)

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
        order_button = self.find_element(MainPageLocators.PLACE_AN_ORDER)
        order_button.click()

        order_number = self.get_text(MainPageLocators.ORDER_ID)

        return order_number

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        ).click()

    @allure.step("Проверить что кнопка оформления заказа активна")
    def is_order_button_active(self):
        return self.find_element(MainPageLocators.PLACE_AN_ORDER).is_enabled()