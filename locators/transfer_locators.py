from selenium.webdriver.common.by import By


class TransferLocators:
    FROM_ACCOUNT_INPUT = (By.ID, "fromAccountId")
    TO_ACCOUNT_INPUT = (By.ID, "toAccountId")
    AMOUNT_INPUT = (By.ID, "amount")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input[type='submit'].button[value='Transfer']")
    TRANSFER_BUTTON_ALT = (By.CSS_SELECTOR, "input[value='Transfer']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "h1")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")
