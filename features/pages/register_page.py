from locators.register_locators import RegisterLocators
from .base_page import BasePage


class RegisterPage(BasePage):
    def open_register_page(self):
        self.open("/register.htm")

    def fill_form(
        self,
        first_name,
        last_name,
        address,
        city,
        state,
        zip_code,
        phone,
        ssn,
        username,
        password,
    ):
        self.fill(RegisterLocators.FIRST_NAME_INPUT, first_name)
        self.fill(RegisterLocators.LAST_NAME_INPUT, last_name)
        self.fill(RegisterLocators.ADDRESS_INPUT, address)
        self.fill(RegisterLocators.CITY_INPUT, city)
        self.fill(RegisterLocators.STATE_INPUT, state)
        self.fill(RegisterLocators.ZIP_CODE_INPUT, zip_code)
        self.fill(RegisterLocators.PHONE_INPUT, phone)
        self.fill(RegisterLocators.SSN_INPUT, ssn)
        self.fill(RegisterLocators.USERNAME_INPUT, username)
        self.fill(RegisterLocators.PASSWORD_INPUT, password)
        self.fill(RegisterLocators.REPEATED_PASSWORD_INPUT, password)

    def submit(self):
        self.click(RegisterLocators.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_page_source()

    def get_error_message(self):
        return self.get_text(RegisterLocators.ERROR_MESSAGE)
