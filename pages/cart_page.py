from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины"""

    # Локаторы
    CART_ITEMS = (By.CSS_SELECTOR, ".cart-item")
    CART_TOTAL = (By.CSS_SELECTOR, ".cart-total__price")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout__button")
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".cart-empty__message")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_cart_items_count(self):
        """Получение количества товаров в корзине"""
        try:
            return len(self.find_elements(self.CART_ITEMS))
        except:
            return 0

    def is_cart_empty(self):
        """Проверка пустоты корзины"""
        try:
            self.find_element(self.EMPTY_CART_MESSAGE)
            return True
        except:
            return False

    def get_cart_total(self):
        """Получение общей суммы корзины"""
        return self.get_text(self.CART_TOTAL)

    def proceed_to_checkout(self):
        """Переход к оформлению заказа"""
        self.click_element(self.CHECKOUT_BUTTON)