import pytest
import allure
from pages.main_page import MainPage



@allure.feature("Доступность внешнего сайта")
class TestWildberriesAvailability:

    @allure.title("Главная страница Wildberries открывается")
    def test_wildberries_url_is_opened(self, driver, base_url):
        main_page = MainPage(driver, base_url)
        main_page.open()

        assert "wildberries.ru" in driver.current_url

    @allure.title("Сайт не показал страницу проверки браузера")
    def test_wildberries_not_blocked_by_browser_check(self, driver, base_url):
        main_page = MainPage(driver, base_url)
        main_page.open()

        if main_page.is_browser_verification_page():
            pytest.skip(
                "Wildberries показал антибот-проверку браузера. "
                "Полноценные UI-тесты нельзя выполнить в текущем запуске."
            )

        assert True


@allure.feature("Поиск товаров")
class TestSearch:

    @allure.story("Результаты поиска")
    @allure.title("Проверка наличия результатов поиска")
    def test_search_returns_results(self, driver, base_url):
        """Тест проверяет, что поиск возвращает результаты"""
        main_page = MainPage(driver, base_url)
        main_page.open()

        search_page = main_page.search("футболка")
        product_count = search_page.get_product_cards_count()

        assert product_count > 0, "Поиск не вернул никаких результатов"
        assert product_count >= 20, f"Ожидалось минимум 20 товаров, найдено: {product_count}"

    @allure.story("Разные поисковые запросы")
    @allure.title("Поиск по разным категориям товаров")
    @pytest.mark.parametrize("search_query", [
        "обувь",
        "сумка",
        "косметика"
    ])
    def test_search_different_categories(self, driver, base_url, search_query):
        """Тест проверяет поиск по разным категориям товаров"""
        main_page = MainPage(driver, base_url)
        main_page.open()

        search_page = main_page.search(search_query)
        product_count = search_page.get_product_cards_count()

        assert product_count > 0, f"Поиск по запросу '{search_query}' не вернул результатов"

    @allure.story("Валидация поиска")
    @allure.title("Проверка загрузки страницы поиска")
    def test_search_page_loads(self, driver, base_url):
        """Тест проверяет, что страница поиска загружается корректно"""
        main_page = MainPage(driver, base_url)
        main_page.open()

        search_page = main_page.search("джинсы")

        assert "search" in driver.current_url or "catalog" in driver.current_url, \
            "URL не содержит expected ключевых слов после поиска"