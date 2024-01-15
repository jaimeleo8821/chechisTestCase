"""
This module contains the LoginHerokuAppPage,
the page object for the HerokuApp login page.
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class LoginHerokuAppPage:

    # URL
    # URL = "https://the-internet.herokuapp.com/basic_auth"
    URL = "https://omayo.blogspot.com/"

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def alertIsPresent(self):
        return WebDriverWait(self.browser, 5).until(EC.alert_is_present())

    def enter_data(self, username, password):
        # alert = Alert(self.browser)
        alert = self.browser.switch_to.alert()
        alert.send_keys(username)
        alert.send_keys(Keys.TAB)
        alert.send_keys(password)

    def press_login_button(self):
        alert = Alert(self.browser)
        # alert = self.browser.switch_to_alert()
        alert.accept()

    def indian_page_method(self):
        prompt = self.browser.find_element(By.ID, 'prompt')
        prompt.click()
        alert = self.browser.switch_to.alert
        # alert.send_keys('indian magic')
        alert.accept()
        sleep(10)
        self.browser.execute_script("""
            
        """)


