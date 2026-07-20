from selenium.webdriver.common.by import By

class RegisterLocators:
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP_CODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#rightPanel h1.title")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#rightPanel > p")
