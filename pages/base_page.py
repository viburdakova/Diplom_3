import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.find_element(locator)
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Кликнуть на элемент в firefox')
    def click_on_element_firefox(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Поиск элемента с ожиданием')
    def cover_elm_with_wait(self, locator):
        browser_name = self.driver.name

        if browser_name == 'firefox':
            self.driver.execute_script("""
                       var l = document.getElementsByClassName("Modal_modal_overlay__x2ZCr")[0];
                       l.parentNode.removeChild(l);
                    """)
        else:
            WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Проверить кликабельность элемента в firefox')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    @allure.step('Проверить отображение элемента в firefox')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(locator).is_displayed()

    @allure.step("Получить текст")
    def get_text(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return element.text

    @allure.step("Отформатировать локатор")
    def format_locator(self, base_locator, number):
        method, locator_template = base_locator
        return (method, locator_template.format(number))

    @allure.step("Проскроллить до элемента и кликнуть")
    def scroll_into_view_and_click(self, locator, locator_to_scroll):
        element_to_scroll = self.find_element(locator_to_scroll)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll)
        self.click_to_element(locator)

    @allure.step("Добавить текст")
    def add_text_element(self, locator, text):
        element = self.find_element(locator)
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Ожидание элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))










