from selenium.webdriver import Chrome
from time import sleep
from selenium_wrapper import SeleniumWrapper

def test_registation_pos(setup):
    s = SeleniumWrapper(setup)
    s.click_ele(("link text","Register"))
    s.click_ele(("id","gender-male"))
    s.enter_text(("id","FirstName"),value="hello")
    s.enter_text(("name","LastName"),value = "P")
    s.enter_text(("name","Email"),value="shobhahdp@gmail.com")
    s.enter_text(("id","Password"),value="shobha123")
    s.enter_text(("id","ConfirmPassword"),value="shobha123")
    s.click_ele(("id","register-button"))



from selenium_wrapper import SeleniumWrapper
from pytest import mark

# eaders = "gender, fname, lname, email, password"
#
# data = [
#     ("male", "steve", "jobs", "steve.jobs@comapny.com", "Password123"),
#     ("female", "laura", "turner", "laura.turner@comapny.com", "Password123")
# ]


# @mark.parametrize(headers, data)
# def test_registration(setup, gender, fname, lname, email, password):
#     s = SeleniumWrapper(setup)
#     s.click_element(("link text", "Register"))
#     if gender == "male":
#         s.click_element(("id", "gender-male"))
#     elif gender == "female":
#         s.click_element(("id", "gender-female"))
#     else:
#         raise Exception("Unknown Gender")
#     s.enter_text(("id", "FirstName"), value=fname)
#     s.enter_text(("id", "LastName"), value=lname)
#     s.enter_text(("id", "Email"), value=email)
#     s.enter_text(("id", "Password"), value=password)
#     s.enter_text(("id", "ConfirmPassword"), value=password)
#     s.click_element(("id", "register-button"))


