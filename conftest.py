import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
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
    return request.config.getoption("--base-url")


@pytest.fixture
def driver(request):
    options = Options()

    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()