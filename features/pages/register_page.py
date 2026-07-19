from locators.register_locators import RegisterLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
    def open_register_page(self):
        self.open("/register.htm")
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(RegisterLocators.FIRST_NAME)
        )

    def fill_registration_form(self, first_name, last_name, address, city, state,
                               zip_code, phone, ssn, username, password, confirm):
        self.fill(RegisterLocators.FIRST_NAME, first_name)
        self.fill(RegisterLocators.LAST_NAME, last_name)
        self.fill(RegisterLocators.ADDRESS, address)
        self.fill(RegisterLocators.CITY, city)
        self.fill(RegisterLocators.STATE, state)
        self.fill(RegisterLocators.ZIP_CODE, zip_code)
        self.fill(RegisterLocators.PHONE, phone)
        self.fill(RegisterLocators.SSN, ssn)
        self.fill(RegisterLocators.USERNAME, username)
        self.fill(RegisterLocators.PASSWORD, password)
        self.fill(RegisterLocators.CONFIRM, confirm)

    def submit_registration(self):
        self.click(RegisterLocators.REGISTER_BUTTON)

    def get_success_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegisterLocators.SUCCESS_MESSAGE)
        )
        return element.text.strip()
