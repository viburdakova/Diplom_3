from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_ITEM = By.XPATH,"//a[contains(@class, 'OrderHistory_link__1iNby')]"
    ORDER_NUMBER_IN_FEED = By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"
    ORDER_NUMBER_IN_MODAL = By.XPATH, "//p[contains(@class, 'text text_type_digits-default mb-10 mt-5')]"
    ORDER_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10')]"
    CLOSE_MODAL_BUTTON = By.XPATH, "//*[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]"
    TOTAL_ORDERS_COUNT = By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p"
    TODAY_ORDERS_COUNT = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDERS_IN_PROGRESS = By.XPATH, "//ul[contains(@class, 'OrderFeed_inProgress')]//li"
    ORDER_NUMBER_IN_ORDER_HISTORY = By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    ORDER_FEED_HEADER = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and contains(text(), 'Лента Заказов')]"