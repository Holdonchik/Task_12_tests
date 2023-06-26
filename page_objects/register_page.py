from selenium.webdriver.common.by import By


class RegisterPage:
    FIRSTNAME_INPUT_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "#register__input-email")
    PHONE_INPUT_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#register__input-password")
    CONFIRM_PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#customer_form > input")
