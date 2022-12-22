import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def app():
    # browser.config.browser_name = 'firefox'
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()