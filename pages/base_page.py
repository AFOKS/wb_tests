from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self, path=""):
        """Открывает страницу по пути"""
        url = f"{self.base_url}{path}"
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Поиск элемента"""
        return self.wait.until(EC.presence_of_element_located(locator), timeout=timeout)

    def find_elements(self, locator, timeout=10):
        """Поиск нескольких элементов"""
        return self.wait.until(EC.presence_of_all_elements_located(locator), timeout=timeout)

    def click_element(self, locator):
        """Клик по элементу"""
        element = self.find_element(locator)
        element.click()

    def input_text(self, locator, text):
        """Ввод текста в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Получение текста элемента"""
        return self.find_element(locator).text

    def get_title(self):
        """Получение заголовка страницы"""
        return self.driver.title