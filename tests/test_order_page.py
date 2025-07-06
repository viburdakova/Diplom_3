import allure

import data
from conftest import driver, order_page, login_page, main_page


class TestOrderPage:

    @allure.feature("Лента заказов")
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталям")
    def test_order_details_modal(self, driver, order_page):
        order_page.get_order_number_in_feed()
        order_page.click_first_order_in_feed()
        assert order_page.is_order_modal_visible()

    @allure.feature("Лента заказов")
    @allure.story("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_in_feed(self, driver, order_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)
        login_page.wait_until_cover_disappears()
        login_page.wait_until_cover_disappears()
        login_page.click_personal_account()

        login_page.wait_until_cover_disappears()
        order_page.go_to_order_history()

        user_orders = order_page.get_history_order_numbers()

        order_page.go_to_order_feed()

        assert order_page.check_orders_in_feed(user_orders)

    @allure.feature("Лента заказов")
    @allure.story("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_total_orders_counter(self, driver, main_page, order_page, login_page):
        login_page.wait_until_cover_disappears()
        main_page.go_to_order_feed()
        start_count_all_orders = order_page.get_total_orders_count()
        login_page.wait_until_cover_disappears()

        login_page.click_personal_account()
        login_page.auth_personal_account(data.log_pass_data)
        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        login_page.wait_until_cover_disappears()

        order_num = main_page.get_order_number()

        main_page.close_modal_window()
        main_page.go_to_order_feed()
        all_orders = order_page.get_total_orders_count()
        assert start_count_all_orders < all_orders

    @allure.feature("Лента заказов")
    @allure.story("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
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

    @allure.feature("Лента заказов")
    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_check_order_in_progress(self, driver, main_page, order_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        order_num = main_page.get_order_number()
        main_page.close_modal_window()
        main_page.go_to_order_feed()
        order_page.find_order_num_in_progress()
        order_nums_in_progress = order_page.get_order_num_in_progress()
        assert f'0{order_num}' == order_nums_in_progress

