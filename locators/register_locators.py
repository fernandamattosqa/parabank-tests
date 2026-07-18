from selenium.webdriver.common.by import By


class RegisterLocators:
    FIRST_NAME_INPUT = (By.NAME, "customer.firstName")
    LAST_NAME_INPUT = (By.NAME, "customer.lastName")
    ADDRESS_INPUT = (By.NAME, "customer.address.street")
    CITY_INPUT = (By.NAME, "customer.address.city")
    STATE_INPUT = (By.NAME, "customer.address.state")
    ZIP_CODE_INPUT = (By.NAME, "customer.address.zipCode")
    PHONE_INPUT = (By.NAME, "customer.phoneNumber")
    SSN_INPUT = (By.NAME, "customer.ssn")
    USERNAME_INPUT = (By.NAME, "customer.username")
    PASSWORD_INPUT = (By.NAME, "customer.password")
    REPEATED_PASSWORD_INPUT = (By.NAME, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")
