import allure

from conftest import driver, main_page, login_page, login_user, create_user
from data import MAIN_URL


class TestMainPage:

    @allure.feature("Основной функционал")
    @allure.title("Навигация по разделам")
    @allure.description("Проверка переключения между разделами 'Конструктор' и 'Лента заказов'")
    def test_navigation(self, main_page):
        main_page.go_to_constructor()
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        assert main_page.current_url() == MAIN_URL

    @allure.feature("Основной функционал")
    @allure.title("Действия с ингредиентами")
    @allure.description("Проверка открытия деталей ингредиента, отображение каунтера и закрытие модального окна")
    def test_ingredient_interaction(self, main_page):
        main_page.go_to_constructor()

        main_page.open_ingredient_details()
        main_page.close_modal_window()

        main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()
        assert main_page.get_ingredient_counter() == 2

    @allure.feature("Основной функционал")
    @allure.title("Создание заказа")
    @allure.description("Проверка создания заказа авторизованным пользователем")
    def test_order_creation(self, main_page, login_page, login_user):

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()

        login_page.wait_until_cover_disappears()
        main_page.place_order()
        order_num = main_page.get_order_number()
        assert order_num != '9999'
