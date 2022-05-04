from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from pytest import mark


class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self,locator):
        super().__init__(locator)
    def __call__(self, driver):
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False

def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver, 10)
        v = _visibility_of_element_located(locator)
        w.until(v)
        return func(*args, **kwargs)
    return wrapper