from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import *


def test_main_page(browser):
    browser.get(browser.url)
    assert WebDriverWait(browser, 1).until(EC.title_is("Opencart.ru: разработка сайтов и модулей на платформе опенкарт"))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.DOWNLOAD_BUTTON))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(MainPage.DEMO_BUTTON))


def test_login_page(browser):
    browser.get(browser.url+"login/")
    assert WebDriverWait(browser, 1).until(EC.title_is("Авторизация"))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LoginPage.EMAIL_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LoginPage.PASSWORD_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(LoginPage.SUBMIT_BUTTON))


def test_register_page(browser):
    browser.get(browser.url+"register/")
    assert WebDriverWait(browser, 1).until(EC.title_is("Регистрация"))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.FIRSTNAME_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.LASTNAME_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.EMAIL_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.PHONE_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.PASSWORD_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.CONFIRM_PASSWORD_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.CONTINUE_BUTTON))

def test_register_page_continue_without_entering_data(browser):
    browser.get(browser.url+"register/")
    el = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.CONTINUE_BUTTON))
    ActionChains(browser).scroll_to_element(el).perform()
    el.click()

    assert WebDriverWait(browser, 1).until(EC.title_is("Регистрация"))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.FIRSTNAME_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.LASTNAME_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.EMAIL_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.PHONE_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.PASSWORD_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.CONFIRM_PASSWORD_INPUT_FIELD))
    assert WebDriverWait(browser, 1).until(EC.visibility_of_element_located(RegisterPage.CONTINUE_BUTTON))


def test_modules_page(browser):
    browser.get(browser.url+"modules/")
    assert WebDriverWait(browser, 1).until(EC.title_is("Модули opencart"))
    el = WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ModulesPage.OPENCART_MODULES_TEXT))
    assert el.text == "Модули opencart"
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ModulesPage.MODULES_CONTENT))

def test_first_object(browser):
    browser.get(browser.url+"modules/")
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(ModulesPage.FIRST_OBJECT)).click()
    el = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(ItemPage.PAGE_TITLE))
    assert el.text == "A-migration – перенос данных с OpenCart 1.5. * на OpenCart 2. * - модуль миграции основных данных"
