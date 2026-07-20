from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from features.pages.base_page import BasePage

class TransferPage(BasePage):
    LINK_TRANSFER = (By.CSS_SELECTOR, "a[href='transfer.htm']")
    AMOUNT_INPUT = (By.ID, "amount")
    FROM_ACCOUNT_INPUT = (By.NAME, "fromAccountId")
    TO_ACCOUNT_INPUT = (By.NAME, "toAccountId")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Transfer']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#showResult h1.title")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "#showError h1.title")

    def open_transfer_page(self):
        """Abre a página de Transfer Funds"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.LINK_TRANSFER)
            )
            element.click()
        except Exception:
            self.open("/transfer.htm")

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.AMOUNT_INPUT)
        )

    def fill_transfer(self, amount: str, from_account: str = None, to_account: str = None):
        """Preenche os campos de transferência"""
        amount_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.AMOUNT_INPUT)
        )
        amount_field.clear()
        amount_field.send_keys(str(amount))

        if from_account:
            from_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.FROM_ACCOUNT_INPUT)
            )
            from_field.send_keys(from_account)

        if to_account:
            to_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.TO_ACCOUNT_INPUT)
            )
            to_field.send_keys(to_account)

    def submit(self):
        """Clica no botão Transfer"""
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TRANSFER_BUTTON)
        )
        button.click()

    def get_success_message(self):
        """Captura mensagem de sucesso"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "showResult"))
            )
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            )
            text = element.text.strip()
            if "Transfer Complete" in text:
                return text
            return None
        except Exception:
            return None

    def get_error_message(self):
        """Captura mensagem de erro (se existir)"""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "showError"))
            )
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            text = element.text.strip()
            if "Error" in text:
                return text
            return None
        except Exception:
            return None
