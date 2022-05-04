# from selenium_wrapper import SeleniumWrapper
# from pytest import mark
# from lib import is_login_success
#
# def test_login_positive(setup):
#     s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
#     s.click_ele(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value="shobhahdp@gmail.com")
#     s.enter_text(("id", "Password"), value="shobha123")
#     s.click_ele(("xpath", "//input[@value='Log in']"))
#
#
# headers = "email, password"
# data = [
#     ("shobhdp@gmail.com", "shobha123"),
#     ("hellowworld", "Passwor12")
#     ]
#
# @mark.parametrize(headers, data)
# def test_login_positive(setup, email, password,sts):
#     s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
#     s.click_ele(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.click_ele(("xpath", "//input[@value='Log in']"))

# from selenium_wrapper import SeleniumWrapper
# from pytest import mark
#
#
# headers = "email, password"
#
# data = [
#     ("shobhahdp@gmail.com", "Password123"),
#     ("shobha123@gmail.com", "123456")
#     ]
#
# @mark.parametrize(headers, data)
# def test_login_positive(setup, email, password):
#     s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
#     s.click_element(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.click_element(("xpath", "//input[@value='Log in']"))
#     if is_login_success(email):
#         print("Success")
#     else:
#         print("FAIL")



#negative
# headers = "email, password,sts"
# data = [
#     ("shobhdp@gmail.com", "shobha123","Login was unsuccessful. Please correct the errors and try again."),
#     ("hworld", "Passwor12","Please enter a valid email address.")
#     ]
#
# @mark.parametrize(headers, data)
# def test_login_positive(setup, email, password,sts):
#     s = SeleniumWrapper(setup)      # SeleniumWrapper(driver)
#     s.click_ele(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.click_ele(("xpath", "//input[@value='Log in']"))


# from _selenium.lib import is_auth_error_displayed
from selenium_wrapper import SeleniumWrapper
from pytest import mark
from lib import is_login_success
from login import LoginPage

headers = "email, password"

data = [
    ("bill.gates@company.com", "Password123"),
    ("hello.world@company.com", "Password123")
]


@mark.parametrize(headers, data)
def test_login_positive(setup, email, password):
    s = SeleniumWrapper(setup)  # SeleniumWrapper(driver)
    s.click_ele(("link text", "Log in"))
    # Call POM functions
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()

    # if is_login_success(email):
    #     print("Success")
    # else:
    #     print("FAIL")

#
# headers = "email, password, error_message"
# data = [
#     ("bill.gates@company.com", "Password12", "Login was unsuccessful. Please correct the errors and try again."),
#     ("hello.world", "Password123", "Please enter a valid email address.")
# ]
#
#
# @mark.parametrize(headers, data)
# def test_login_positive(setup, email, password, error_message):
#     s = SeleniumWrapper(setup)  # SeleniumWrapper(driver)
#     s.click_element(("link text", "Log in"))
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.click_element(("xpath", "//input[@value='Log in']"))
    # if is_auth_error_displayed(error_message):
    #     print("PASS")
    # else:
    #     print("FAIL")