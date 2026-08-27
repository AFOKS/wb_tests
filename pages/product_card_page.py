from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductCardPage(BasePage):
    """Страница карточки товара"""

    # Локаторы
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product-detail__name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price__current")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart__button")
    SIZE_SELECTOR = (By.CSS_SELECTOR, ".size-selector__button")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".product-images__image")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, ".product-description__text")
    RATING_STARS = (By.CSS_SELECTOR, ".rating__stars")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_product_title(self):
        """Получение названия товара"""
        return self.get_text(self.PRODUCT_TITLE)

    def get_product_price(self):
        """Получение цены товара"""
        return self.get_text(self.PRODUCT_PRICE)

    def add_to_cart(self):
        """Добавление товара в корзину"""
        self.click_element(self.ADD_TO_CART_BUTTON)

    def select_size(self, size_index=0):
        """Выбор размера"""
        sizes = self.find_elements(self.SIZE_SELECTOR)
        if sizes:
            sizes[size_index].click()

    def is_images_loaded(self):
        """Проверка загрузки изображений"""
        images = self.find_elements(self.PRODUCT_IMAGES)
        return len(images) > 0

    def get_rating(self):
        """Получение рейтинга товара"""
        return self.get_text(self.RATING_STARS)