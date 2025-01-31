import os
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()

    # Если в переменной окружения HEADLESS указано "true", запускаем в headless
    if os.getenv("HEADLESS", "false").lower() == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://github.com")

    yield

    browser.quit()
