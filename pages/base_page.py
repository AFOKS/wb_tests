from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        self.driver.get(f"{self.base_url}{path}")

    def find_element(self, locator, timeout=10):
        """Ждёт появления и видимости одного элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        """Ждёт появления хотя бы одного элемента и возвращает список"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, timeout=10):
        """Ждёт кликабельности и кликает по элементу"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text, timeout=10):
        """Ввод текста в поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    def get_title(self):
        return self.driver.title