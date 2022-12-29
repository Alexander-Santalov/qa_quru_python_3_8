import sys

from selene.support.shared import browser
from selenium.webdriver import Keys


def set_date(selector, date):
    browser.element(selector).send_keys(
        Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a').type(date).press_enter()
