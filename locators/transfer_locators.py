from selenium.webdriver.common.by import By

class TransferLocators:
    LINK_TRANSFER = (By.CSS_SELECTOR, "a[href='transfer.htm']")
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT_INPUT = (By.NAME, "fromAccountId")
    TO_ACCOUNT_INPUT = (By.NAME, "toAccountId")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Transfer']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#showResult h1.title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#showError h1.title")
