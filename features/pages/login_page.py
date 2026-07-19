from locators.login_locators import LoginLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def open_login_page(self):
        self.open("/index.htm")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(LoginLocators.USERNAME_INPUT)
        )

    def fill_credentials(self, username, password):
        self.fill(LoginLocators.USERNAME_INPUT, username)
        self.fill(LoginLocators.PASSWORD_INPUT, password)

    def login(self, username, password):
        self.fill_credentials(username, password)
        self.click_login_button()

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(LoginLocators.LOGIN_BUTTON)
        )
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE)
            )
            return element.text.strip()
        except:
            return ""

    def is_logged_in(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(LoginLocators.WELCOME_MESSAGE)
            )
            return element.text.startswith("Welcome") or element.text.startswith("Accounts Overview")
        except:
            return False

    def logout(self):
        if self.get_element_or_none(LoginLocators.LOGOUT_LINK):
            self.click(LoginLocators.LOGOUT_LINK)
            try:
                self.validate_url("login")
            except AssertionError:
                if "index.htm" in self.driver.current_url:
                    self.driver.get(f"{self.base_url}/index.htm")
                self.validate_url("index")

    def get_login_title(self):
        try:
            return self.get_text(LoginLocators.LOGIN_TITLE)
        except:
            return ""
