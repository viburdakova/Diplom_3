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

    @allure.step("Получение текущего url")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.find_element(locator)
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Перетаскивание ингредиентов в firefox")
    def drag_and_drop_element_firefox(self, source_element, target_element):
        script = """
                    function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                        var dataTransfer = new DataTransfer();
                        var dragStartEvent = new DragEvent('dragstart', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragStartEvent);

                        var dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        destinationNode.dispatchEvent(dropEvent);
        				var dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer
                        });
                        sourceNode.dispatchEvent(dragEndEvent);
                    }
                    simulateHTML5DragAndDrop(arguments[0], arguments[1]);
                    """
        self.driver.execute_script(script, source_element, target_element)

    @allure.step("Перетаскивание ингредиентов")
    def drag_and_drop(self, locator_from, locator_to):
        element_from = self.find_element(locator_from)
        element_to = self.find_elememt(locator_to)

        self.driver.drag_and_drop(element_from, element_to).perfom()

    @allure.step("Ожидание когда элемент станет видимым")
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание когда элемент станет невидимым")
    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step("Клик")
    def get_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание когда элемент станет кликабельным")
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

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










