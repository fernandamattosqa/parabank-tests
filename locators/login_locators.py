from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value='Log In']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")
    ACCOUNTS_OVERVIEW = (By.LINK_TEXT, "Accounts Overview")
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")
