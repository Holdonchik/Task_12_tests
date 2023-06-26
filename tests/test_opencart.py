import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import *

def test_main_page(browser):
    browser.get(browser.url)
    el = WebDriverWait(driver=browser, timeout=5).until(method=EC.visibility_of_element_located(MainPage.MAIN_PAGE_TEXT))
    assert el.text.lower() == "современная платформа для создания готового интернет-магазина"
    assert "Opencart.ru: разработка сайтов и модулей на платформе опенкарт" in browser.title

def test_login_page(browser):
    browser.get(browser.url+"login/")
    assert "Авторизация" in browser.title

def test_register_page(url, browser):
    browser.get(browser.url+"register/")
    el = WebDriverWait(driver=browser, timeout=5).until(
        method=EC.visibility_of_element_located(MainPage.MAIN_PAGE_TEXT))
    assert el.text.lower() == "современная платформа для создания готового интернет-магазина"
    assert "Opencart.ru: разработка сайтов и модулей на платформе опенкарт" in browser.title

