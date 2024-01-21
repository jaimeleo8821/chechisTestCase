"""
This module contains the ResultLoginHerokuAppPage,
the page object for the result of the HerokuApp login page.
"""

from selenium.webdriver.common.by import By
from time import sleep


class ResultLoginHerokuAppPage:
    script = "return window.getComputedStyle(document.getElementById('flash'), '::before').getPropertyValue('content')"
    MESSAGE = (By.ID, "flash")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Method that capture the text inside a Flash message
    # using Javascript Executor
    def capture_flash_message(self):
        message = self.browser.execute_script(self.script)
        sleep(1)
        msg = str(message)
        return msg

    # Method that capture the text inside a Flash message
    # using Selenium
    def capture_message(self):
        sleep(1)
        message = self.browser.find_element(*self.MESSAGE).text
        msg = message.strip()
        return msg
