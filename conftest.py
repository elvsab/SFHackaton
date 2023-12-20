import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("driver")
    if browser_name == "chrome":
        driver_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
    elif browser_name == "firefox":
        driver_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=driver_service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.get("https://dima731515.github.io/hakaton/html/")

    yield driver
    driver.quit()
