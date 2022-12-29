from selene import have
from selene.support.shared import browser


def set_checkboxes(locator, list_value):
    for hobby in list_value:
        browser.all(locator).element_by(have.exact_text(hobby)).click()




