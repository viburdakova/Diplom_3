

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_page_locators import LoginPageLocators

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Кликнуть на первый заказ в ленте")
    def click_first_order_in_feed(self):
        first_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_ITEM)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", first_order)
        first_order.click()

    @allure.step("Получить номер заказа в ленте")
    def get_order_number_in_feed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_NUMBER_IN_FEED)
        ).text

    @allure.step("Проверить видимость модального окна")
    def is_order_modal_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_MODAL_WINDOW)
        ).is_displayed()

    @allure.step("Получить номер заказа в модальном окне")
    def get_order_number_in_modal(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_NUMBER_IN_MODAL)
        ).text

    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CLOSE_MODAL_BUTTON)
        ).click()

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.ORDER_HISTORY)
        ).click()
        WebDriverWait(self.driver, 20).until(EC.url_contains("/account/order-history"))

    @allure.step("Получить номера заказов из истории")
    def get_history_order_numbers(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.ORDER_NUMBER_IN_ORDER_HISTORY)
        )
        return [el.text for el in elements]

    @allure.step("Перейти в ленту заказов")
    def go_to_order_feed(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(OrderPageLocators.ORDER_FEED_HEADER)
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(OrderPageLocators.ORDER_FEED_HEADER)
        )

    @allure.step("Получить номера заказов из ленты")
    def get_feed_order_numbers(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.ORDER_NUMBER_IN_FEED)
        )
        return [el.text for el in elements]

    @allure.step("Проверить наличие заказов в ленте")
    def check_orders_in_feed(self, order_numbers):
        feed_orders = self.get_feed_order_numbers()
        return any(order in feed_orders for order in order_numbers)

    @allure.step("Получить текущее значение счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        all_orders_num = self.get_text(OrderPageLocators.TOTAL_ORDERS_COUNT)
        return all_orders_num

    @allure.step("Получить текущее значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        count_text = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.TODAY_ORDERS_COUNT)
        ).text
        return int(count_text)

    @allure.step("Получить значение номера заказа 'в работе)")
    def get_order_num_in_progress(self):
        self.wait_for_clickable(OrderPageLocators.ORDERS_IN_PROGRESS)
        return self.wait_for_visible(OrderPageLocators.ORDERS_IN_PROGRESS).text