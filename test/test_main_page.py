import allure
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPage:

    @allure.story("Открытие главной страницы")
    @allure.title("Проверка открытия главной страницы")
    def test_main_page_opens(self, driver, base_url):
        main_page = MainPage(driver, base_url)
        main_page.open()

        print("URL:", driver.current_url)
        print("TITLE:", driver.title)

        driver.save_screenshot("wb_page.png")

        assert "wildberries.ru" in driver.current_url

    @allure.story("Элементы главной страницы")
    @allure.title("Проверка видимости логотипа")
    def test_logo_is_visible(self, driver, base_url):
        """Тест проверяет, что логотип виден на главной странице"""
        main_page = MainPage(driver, base_url)
        main_page.open()

        assert main_page.is_logo_visible(), "Логотип не виден на странице"

    @allure.story("Поиск на главной странице")
    @allure.title("Проверка работы поиска")
    def test_search_functionality(self, driver, base_url):
        """Тест проверяет, что поиск работает корректно"""
        main_page = MainPage(driver, base_url)
        main_page.open()

        search_page = main_page.search("платье")

        assert search_page.is_search_results_loaded(), \
            "Результаты поиска не загрузились"