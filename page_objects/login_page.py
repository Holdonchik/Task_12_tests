from selenium.webdriver.common.by import By


class LoginPage:
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#login__input-email")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#login__input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#login > input.btn.btn-primary")
