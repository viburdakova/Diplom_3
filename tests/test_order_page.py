import allure

from conftest import driver, order_page, login_user, main_page, login_page, create_user, create_order


class TestOrderPage:

    @allure.feature("Лента заказов")
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталям")
    def test_order_details_modal(self, order_page):
        order_page.get_order_number_in_feed()
        order_page.click_first_order_in_feed()
        assert order_page.is_order_modal_visible()

    @allure.feature("Лента заказов")
    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_orders_in_feed(self, create_order, order_page, login_user, login_page):
        login_page.wait_until_cover_disappears()
        login_page.wait_until_cover_disappears()
        login_page.click_personal_account()

        order_page.go_to_order_history()
        user_orders = order_page.get_history_order_numbers()
        order_page.go_to_order_feed()
        assert order_page.check_orders_in_feed(user_orders)

    @allure.feature("Лента заказов")
    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter(self, main_page, order_page, login_page, login_user):
        login_page.wait_until_cover_disappears()
        login_page.wait_until_cover_disappears()
        main_page.go_to_order_feed()
        current_count_all_orders = order_page.get_total_orders_count()
        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.go_to_order_feed()
        all_orders = order_page.get_total_orders_count()
        assert current_count_all_orders < all_orders

    @allure.feature("Лента заказов")
    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter(self, main_page, order_page, login_page, login_user):
        order_page.go_to_order_feed()
        today_count_orders = order_page.get_today_orders_count()
        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        main_page.place_order()
        main_page.go_to_order_feed()
        new_today_count = order_page.get_today_orders_count()
        assert new_today_count > today_count_orders

    @allure.feature("Лента заказов")
    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_check_order_in_progress(self, main_page, order_page, login_page, login_user):
        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()
        order_number = main_page.place_order()
        main_page.go_to_order_feed()
        order_num_in_progress = order_page.get_order_num_in_progress()
        assert order_number > order_num_in_progress

