from Driver.driver import browser_setup
from Base.base import BaseSetup
from Locator.locators import MainLoginPageLocators


class LoginPage(BaseSetup):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator_main = MainLoginPageLocators

    def login_user(self, login, password):
        self.click_to_element(*self.locator_main.SIGNIN)
        self.send_keys_to(login, *self.locator_main.EMAIL)
        self.send_keys_to(password, *self.locator_main.PASSWORD)
        self.click_to_element(*self.locator_main.BUTTON_SIGIN)

    def check_log_in_user(self):
        return True if self.find_element(*self.locator_main.PROFILE).text == ' Profile' else False

    def check_log_in_admin(self):
        return True if self.find_element(*self.locator_main.CATEGORIES).text == ' Categories' else False








