from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from locators.transfer_locators import TransferLocators
from .base_page import BasePage


class TransferPage(BasePage):
    def open_transfer_page(self):
        locators = [
            (By.LINK_TEXT, "Transfer Funds"),
            (By.PARTIAL_LINK_TEXT, "Transfer"),
            (By.CSS_SELECTOR, "a[href*='transfer']"),
        ]

        clicked = False
        for locator in locators:
            try:
                element = WebDriverWait(self.driver, 8).until(EC.element_to_be_clickable(locator))
                element.click()
                clicked = True
                break
            except Exception:
                continue

        if not clicked:
            self.open("/transfer.htm")

        self.wait_for_element(TransferLocators.AMOUNT_INPUT, timeout=10)

    def fill_transfer(self, from_account, to_account, amount):
        self.wait_for_element(TransferLocators.FROM_ACCOUNT_INPUT)
        self.wait_for_element(TransferLocators.TO_ACCOUNT_INPUT)
        Select(self.driver.find_element(*TransferLocators.FROM_ACCOUNT_INPUT)).select_by_value(str(from_account))
        Select(self.driver.find_element(*TransferLocators.TO_ACCOUNT_INPUT)).select_by_value(str(to_account))
        self.fill(TransferLocators.AMOUNT_INPUT, str(amount))

    def submit(self):
        button = self.get_element_or_none(TransferLocators.TRANSFER_BUTTON)
        if button:
            button.click()
            return
        self.click(TransferLocators.TRANSFER_BUTTON_ALT)

    def get_success_message(self):
        return self.get_page_source()

    def get_error_message(self):
        return self.get_text(TransferLocators.ERROR_MESSAGE)
