from selenium.webdriver.common.by import By


class ModulesPage:
    OPENCART_MODULES_TEXT = (By.CSS_SELECTOR, ".blog__page-title")
    MODULES_CONTENT = (By.CSS_SELECTOR, "#content\ category__content")
    FIRST_OBJECT = (By.PARTIAL_LINK_TEXT, "A-migration – перенос данных с OpenCart 1.5. * на ..")