from selenium.webdriver import Chrome
from time import sleep
from pytest import fixture

@fixture
def setup():
    driver = Chrome(r"chromedriver.exe")
    driver.maximize_window()
    driver.get("http://demowebshop.tricentis.com/")
    sleep(3)
    yield driver
    driver.close()