"""
These test cover a fail login in the web page
https://the-internet.herokuapp.com/login
"""
import pytest

from pages.login import LoginHerokuAppPage
from pages.result_login import ResultLoginHerokuAppPage


# message = "\uf057" is a code for the content of the flash message
@pytest.mark.parametrize('username,password,message', [('alansmith', 'Password!', '"\uf057"')])
def test_fail_web_login(browser, username, password, message):
    login_page = LoginHerokuAppPage(browser)
    result_login_page = ResultLoginHerokuAppPage(browser)

    # Given the login page loaded
    login_page.load()

    # When the user enter a username and password
    login_page.enter_data(username, password)

    # And click on the Login in button
    login_page.click_login_button()

    # Then a successful login page is displayed
    assert message in result_login_page.capture_flash_message()
