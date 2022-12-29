from selene import have, be
from selene.support.shared import browser

from demoqa_tests.model.methods import checkbox
from demoqa_tests.model.methods import dropdown
from demoqa_tests.model.methods import radio
from demoqa_tests.model.methods import datepicker
from demoqa_tests.utils import path_generate


def opening():
    browser.open("/automation-practice-form")


def input_name(value):
    browser.element("#firstName").set_value(value)


def input_surname(value):
    browser.element("#lastName").set_value(value)


def input_mail(value):
    browser.element("#userEmail").set_value(value)


def set_gender(value):
    radio.set_radio('[name=gender]', value)


def input_phone(value):
    browser.element("#userNumber").set_value(value)


def input_date(date):
    datepicker.set_date("#dateOfBirthInput", date)


def input_subject(value):
    browser.element("#subjectsInput").type(value)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(value)).should(be.visible)
    browser.element("#subjectsInput").press_tab()


def set_hobby(list_value):
    checkbox.set_checkboxes("[for^=hobbies-checkbox]", list_value)


def send_image(name_file):
    browser.element("#uploadPicture").set_value(path_generate.generate_path_upload(name_file))


def input_address(value):
    browser.element("#currentAddress").set_value(value)


def select_state(value):
    dropdown.select_value_from_drop_down_list('#state', '[id^=react-select][id*=option]', value)


def select_city(value):
    dropdown.select_value_from_drop_down_list('#city', '[id^=react-select][id*=option]', value)


def submit():
    browser.element('#submit').press_enter()


def fill_registration_form(*, name, surname, mail, gender, phone, birthday, subject, hobby, name_file,
                           address, state, city):
    input_name(name)
    input_surname(surname)
    input_mail(mail)
    set_gender(gender)
    input_phone(phone)
    input_date(birthday)
    input_subject(subject)
    set_hobby(hobby)
    send_image(name_file)
    input_address(address)
    select_state(state)
    select_city(city)
    submit()


def assert_results_registration(equal: int, *values: str):
    browser.all("tbody tr").should(have.size(equal))
    browser.all("tbody tr td:last-child").should(have.exact_texts(values))
