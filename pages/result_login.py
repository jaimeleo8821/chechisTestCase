"""
This module contains the ResultLoginHerokuAppPage,
the page object for the result of the HerokuApp login page.
"""

from selenium.webdriver.common.by import By


class ResultLoginHerokuAppPage:
    FLASH_MESSAGE = (By.ID, "flash")
    SUCCESSFUL_MESSAGE = "You logged into a secure area!"
    ERROR_MESSAGE = "Your username is invalid!"
    script = "return window.getComputedStyle(document.getElementById('flash'), '::before').getPropertyValue('content')"

    def __init__(self, browser):
        self.browser = browser

    def capture_flash_message(self):
        # message = self.browser.find_element(*self.FLASH_MESSAGE)
        message = self.browser.execute_script(self.script)
        # value = message.get_attribute('value')
        msg = str(message)
        print(msg)
        return msg
