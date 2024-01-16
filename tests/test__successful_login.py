"""
These test cover a successful login in the web page
https://the-internet.herokuapp.com/basic_auth
"""
from pages.login import LoginHerokuAppPage
from time import sleep


def test_successful_web_login(browser):
    login_page = LoginHerokuAppPage(browser)

    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"

    # Given the login page loaded
    login_page.load()

    # When the user enter a valid username and password
    login_page.enter_data(USERNAME, PASSWORD)

    # And click on the Login in button
    login_page.click_login_button()

    # Then a successful login page is displayed
