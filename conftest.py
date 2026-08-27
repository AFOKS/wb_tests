import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """Добавляем кастомные опции для запуска"""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск браузера в headless режиме"
    )
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.wildberries.ru",
        help="Базовый URL для тестов"
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Фикстура для базового URL"""
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    """Фикстура для WebDriver с настройками Chrome"""
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()