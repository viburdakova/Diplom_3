from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_ITEM = By.XPATH,"//a[contains(@class, 'OrderHistory_link__1iNby')]"
    ORDER_NUMBER_IN_FEED = By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"
    ORDER_NUMBER_IN_MODAL = By.XPATH, "//p[contains(@class, 'text text_type_digits-default mb-10 mt-5')]"
    ORDER_MODAL_WINDOW = By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10')]"
    CLOSE_MODAL_BUTTON = By.XPATH, "//*[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]"
    TOTAL_ORDERS_COUNT = By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    TODAY_ORDERS_COUNT = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDER_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDERS_IN_PROGRESS = By.XPATH, "//*[contains(@class,'orderListReady')]//li[contains(@class,'digits-default')]"
    ORDER_NUMBER_IN_ORDER_HISTORY = By.XPATH, "//p[contains(@class, 'text text_type_digits-default')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//*[text()='Оформить заказ']"
    ORDER_FEED_HEADER = By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and contains(text(), 'Лента Заказов')]"
    ORDER_MODAL = (By.XPATH, '//div[contains(@class,"Modal_modal__container__Wo2l_")]')
    DEFAULT_ORDER_NUMBER = (By.XPATH, '//h2[text()="9999"]')
    ACTUAL_ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "type_digits-large")]')