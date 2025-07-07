from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR = By.XPATH, "//*[text()='Конструктор']"
    ASSEMBLE_BURGER = By.XPATH, "//*[text()='Соберите бургер']"
    ORDER_FEED_BUTTON = By.XPATH, "//*[text()='Лента Заказов']"
    ORDER_FEED = By.XPATH, "//*[text()='Лента заказов']"
    INGREDIENT_ITEM = By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient__')]"
    INGREDIENT_COUNTER = By.XPATH, ".//*[contains(@class, 'counter_counter__')]"
    MODAL_WINDOW = By.XPATH, "//*[contains(@class, 'Modal_modal__')]"
    MODAL_CLOSE_BUTTON = By.XPATH, "//button[contains(@class,'close')]"
    PLACE_AN_ORDER = By.XPATH, "//*[text()='Оформить заказ']"
    BURGER_CONSTRUCTOR = By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__')]"
    ORDER_ID = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]"
    MODAL_TITLE_SHADOW = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]"


