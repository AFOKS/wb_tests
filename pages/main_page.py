from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница Wildberries"""

    # Локаторы
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-bar__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-bar__button")
    HEADER_LOGO = (By.CSS_SELECTOR, ".header-navbar__logo")
    CART_BUTTON = (By.CSS_SELECTOR, ".cart-icon")
    CATALOG_BUTTON = (By.CSS_SELECTOR, ".catalog-menu__button")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open(self):
        """Открывает главную страницу"""
        super().open("/")

    def search(self, query):
        """Выполняет поиск"""
        self.input_text(self.SEARCH_INPUT, query)
        self.click_element(self.SEARCH_BUTTON)
        from pages.search_page import SearchPage
        return SearchPage(self.driver, self.base_url)

    def go_to_cart(self):
        """Переход в корзину"""
        self.click_element(self.CART_BUTTON)
        from pages.cart_page import CartPage
        return CartPage(self.driver, self.base_url)

    def is_logo_visible(self):
        """Проверка видимости логотипа"""
        return self.find_element(self.HEADER_LOGO).is_displayed()