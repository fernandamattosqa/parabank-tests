from locators.login_locators import LoginLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def open_login_page(self):
        self.open("/")
        if self.is_logged_in():
            return

    def fill_credentials(self, username, password):
        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)

    def login(self, username, password):
        self.fill_credentials(username, password)
        self.click_login_button()

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        message = self.get_text(LoginLocators.ERROR_MESSAGE)
        if message:
            return message
        if "Error" in self.get_page_source():
            return "Error"
        return ""

    def is_logged_in(self):
        return self.get_element_or_none(LoginLocators.ACCOUNTS_OVERVIEW) is not None or "Accounts Overview" in self.get_page_source()

    def logout(self):
        if self.get_element_or_none(LoginLocators.LOGOUT_LINK):
            self.click(LoginLocators.LOGOUT_LINK)
            try:
                self.validate_url("login")
            except AssertionError:
                if "index.htm" in self.driver.current_url:
                    self.driver.get(f"{self.base_url}/index.htm")
                self.validate_url("index")
