"""
These test cover a successful login in the web page
https://the-internet.herokuapp.com/login
"""
import pytest

from pages.login import LoginHerokuAppPage
from pages.result_login import ResultLoginHerokuAppPage


@pytest.mark.parametrize('username,password,message', [('tomsmith', 'SuperSecretPassword!', 'You logged into a secure area!')])
def test_successful_web_login(browser, username, password, message):
    login_page = LoginHerokuAppPage(browser)
    result_login_page = ResultLoginHerokuAppPage(browser)

    # Given the login page loaded
    login_page.load()

    # When the user enter a valid username and password
    login_page.enter_data(username, password)

    # And click on the Login in button
    login_page.click_login_button()

    # Then a successful login page is displayed
    assert message in result_login_page.capture_message()
