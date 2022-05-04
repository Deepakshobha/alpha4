from wait import wait
from selenium.webdriver.support.select import Select


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self,locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def click_ele(self,locator):
        self.driver.find_element(*locator).click()

    @wait
    def select_item(self,locator,*,item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        s.select_by_visible_text(item)