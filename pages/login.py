"""
This module contains the LoginHerokuAppPage,
the page object for the HerokuApp login page.
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginHerokuAppPage:

    # URL
    URL = "https://the-internet.herokuapp.com/login"
    INPUT_USERNAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def enter_data(self, username, password):
        input_username = self.browser.find_element(*self.INPUT_USERNAME)
        input_password = self.browser.find_element(*self.INPUT_PASSWORD)
        input_username.send_keys(username + Keys.TAB)
        input_password.send_keys(password)

    def click_login_button(self):
        button = self.browser.find_element(*self.LOGIN_BUTTON)
        button.click()
