from selenium.webdriver import ActionChains
from base_check import CheckElement
from page_objects import *


def test_main_page(browser):
    browser.get(browser.url)
    page_objects = {MainPage.DOWNLOAD_BUTTON,
                    MainPage.DEMO_BUTTON}
    assert CheckElement.check_elements(browser, 1, page_objects)


def test_login_page(browser):
    browser.get(browser.url+"login/")
    page_objects = [LoginPage.EMAIL_INPUT_FIELD, LoginPage.PASSWORD_INPUT_FIELD, LoginPage.SUBMIT_BUTTON ]
    assert CheckElement.check_elements(browser, 1, page_objects)


def test_register_page(browser):
    browser.get(browser.url+"register/")
    page_objects = {RegisterPage.FIRSTNAME_INPUT_FIELD,
                    RegisterPage.LASTNAME_INPUT_FIELD,
                    RegisterPage.EMAIL_INPUT_FIELD,
                    RegisterPage.PHONE_INPUT_FIELD,
                    RegisterPage.PASSWORD_INPUT_FIELD,
                    RegisterPage.CONFIRM_PASSWORD_INPUT_FIELD,
                    RegisterPage.CONTINUE_BUTTON}
    assert CheckElement.check_elements(browser, 1, page_objects)


def test_register_page_continue_without_entering_data(browser):
    browser.get(browser.url+"register/")
    el = CheckElement.check_element(browser, 1, RegisterPage.CONTINUE_BUTTON)
    ActionChains(browser).scroll_to_element(el).perform()
    el.click()

    page_objects = {RegisterPage.FIRSTNAME_INPUT_FIELD,
                    RegisterPage.LASTNAME_INPUT_FIELD,
                    RegisterPage.EMAIL_INPUT_FIELD,
                    RegisterPage.PHONE_INPUT_FIELD,
                    RegisterPage.PASSWORD_INPUT_FIELD,
                    RegisterPage.CONFIRM_PASSWORD_INPUT_FIELD,
                    RegisterPage.CONTINUE_BUTTON}
    assert CheckElement.check_elements(browser, 1, page_objects)


def test_modules_page(browser):
    browser.get(browser.url+"modules/")
    page_objects = {ModulesPage.OPENCART_MODULES_TEXT,
                    ModulesPage.MODULES_CONTENT}
    assert CheckElement.check_elements(browser, 1, page_objects)


def test_first_object(browser):
    browser.get(browser.url+"modules/")
    CheckElement.check_element(browser, 1, ModulesPage.FIRST_OBJECT).click()
    el = CheckElement.check_element(browser, 1, ItemPage.PAGE_TITLE)
    assert el.text == "A-migration – перенос данных с OpenCart 1.5." \
                      " * на OpenCart 2. * - модуль миграции основных данных"
