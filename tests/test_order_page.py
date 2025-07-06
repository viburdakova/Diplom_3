import allure

import data
from conftest import driver, order_page, login_page, main_page


class TestOrderPage:

    @allure.feature("Лента заказов")
    @allure.title("Просмотр деталей заказа")
    def test_order_details_modal(self, driver, order_page):
        order_page.get_order_number_in_feed()
        order_page.click_first_order_in_feed()
        assert order_page.is_order_modal_visible()

    @allure.feature("Лента заказов")
    @allure.story("Отображение заказов пользователя")
    def test_user_orders_in_feed(self, driver, order_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)
        login_page.wait_until_cover_disappears()
        login_page.click_personal_account()

        order_page.go_to_order_history()

        user_orders = order_page.get_history_order_numbers()
        assert user_orders

        order_page.go_to_order_feed()

        assert order_page.check_orders_in_feed(user_orders)

    @allure.feature("Лента заказов")
    @allure.story("Счетчик всего выполненных заказов")
    def test_total_orders_counter(self, driver, main_page, order_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_modal_window()
        main_page.go_to_order_feed()

        initial_count = order_page.get_total_orders_count()

        new_count = order_page.get_total_orders_count()
        assert new_count > initial_count, (
                f"Было: {initial_count}, стало: {new_count}")

    @allure.feature("Лента заказов")
    @allure.story("Счетчик заказов выполненных за сегодня")
    def test_today_orders_counter(self, driver, main_page, order_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.close_modal_window()
        main_page.go_to_order_feed()

        initial_count = order_page.get_today_orders_count()
        new_count = order_page.get_today_orders_count()
        assert new_count == initial_count + 1, (
            f"Ожидалось: {initial_count + 1}, получено: {new_count}")

    #@allure.feature("Лента заказов")
    #@allure.title("После оформления заказа его номер появляется в разделе В работе")
    #def test_
