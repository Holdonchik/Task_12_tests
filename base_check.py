from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckElement:
    @staticmethod
    def check_elements(browser, timeout, page_objects):

        for page_object in page_objects:
            try:
                return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(page_object))
            except TimeoutException:

                assert False

    @staticmethod
    def check_element(browser, timeout, page_object):
        try:
            return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(page_object))
        except TimeoutException:
            assert False
