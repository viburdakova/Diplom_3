import allure
import pytest

import data
from conftest import driver, main_page, login_page

class TestMainPage:

    @allure.feature("Основной функционал")
    @allure.title("Навигация по разделам")
    @allure.description("Проверка переключения между разделами 'Конструктор' и 'Лента заказов'")
    def test_navigation(self, driver, main_page):
        main_page.go_to_constructor()
        main_page.go_to_order_feed()
        main_page.go_to_constructor()

    @allure.feature("Основной функционал")
    @allure.title("Действия с ингредиентами")
    @allure.description("Проверка открытия деталей ингредиента и отображение каунтера")
    def test_ingredient_interaction(self, driver, main_page):
        main_page.go_to_constructor()

        main_page.open_ingredient_details()
        main_page.close_modal_window()

        main_page.get_ingredient_counter()
        main_page.add_ingredient_to_order()

    @allure.feature("Основной функционал")
    @allure.title("Создание заказа")
    @allure.description("Проверка создания заказа авторизованным пользователем")
    def test_order_creation(self, driver, main_page, login_page):
        login_page.auth_personal_account(data.log_pass_data)

        main_page.go_to_constructor()
        main_page.add_ingredient_to_order()

        main_page.place_order()
        main_page.close_modal_window()