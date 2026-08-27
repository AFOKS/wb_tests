from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    """Страница результатов поиска"""

    # Локаторы
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".[product_card]")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".product-card:first-child")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".sorting__button")
    FILTER_PRICE_FROM = (By.CSS_SELECTOR, "input[data-name='priceFrom']")
    FILTER_PRICE_TO = (By.CSS_SELECTOR, "input[data-name='priceTo']")
    FILTER_APPLY = (By.CSS_SELECTOR, ".filter__button--apply")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_product_cards_count(self):
        """Получение количества карточек товаров"""
        return len(self.find_elements(self.PRODUCT_CARDS))

    def open_first_product(self):
        """Открытие первой карточки товара"""
        self.click_element(self.FIRST_PRODUCT)
        from pages.product_card_page import ProductCardPage
        return ProductCardPage(self.driver, self.base_url)

    def is_search_results_loaded(self):
        """Проверка загрузки результатов поиска"""
        try:
            self.find_elements(self.PRODUCT_CARDS, timeout=5)
            return True
        except:
            return False

    def get_first_product_name(self):
        """Получение названия первого товара"""
        return self.get_text((By.CSS_SELECTOR, ".product-card:first-child .product-card__name"))