from selene import have
from selene.support.shared import browser


def set_checkboxes(locator, list_value):
    for hobby in list_value:
        browser.all(locator).element_by(have.exact_text(hobby)).click()


def select_value_from_drop_down_list(locator, locator_option,  value):
    browser.element(locator).click()
    browser.all(locator_option).element_by(have.exact_text(value)).click()

