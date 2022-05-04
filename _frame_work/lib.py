from time import sleep
from selenium.common.exceptions import NoSuchElementException
driver = "chromedriver.exe"

def is_login_success(email):
    """
    Returns True if the user is logged in successfully else returns False
    """
    _xpath = f"//a[text()='{email}']"   # //a[text()='bill.gates@company.com']
    for _ in range(10):
        try:
            driver.find_element_by_xpath(_xpath).is_displayed()
            return True
        except NoSuchElementException:
            sleep(1)
            continue
    return False


