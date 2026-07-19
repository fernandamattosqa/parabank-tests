from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import click_element, fill_field, get_element_or_none, get_text, logger


class BasePage:
    def __init__(self, driver, base_url="https://parabank.parasoft.com/parabank"):
        # Define a URL padrão do Parabank oficial
        self.driver = driver
        self.base_url = base_url

    def open(self, path=""):
        # Abre a URL completa (base_url + path)
        self.driver.get(f"{self.base_url}{path}")

    def wait_for_element(self, locator, timeout=20):
        # Espera o elemento estar visível
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=20):
        return click_element(self.driver, locator, timeout)

    def fill(self, locator, value, timeout=20):
        return fill_field(self.driver, locator, value, timeout)

    def get_text(self, locator, timeout=20):
        try:
            return get_text(self.driver, locator, timeout)
        except (NoSuchElementException, TimeoutException):
            logger.warning(f"Texto não encontrado para o locator {locator}")
            return ""

    def get_element_or_none(self, locator, timeout=20):
        return get_element_or_none(self.driver, locator, timeout)

    def get_page_source(self):
        return self.driver.page_source

    def validate_url(self, expected_fragment):
        if expected_fragment not in self.driver.current_url:
            raise AssertionError(
                f"Expected URL to contain '{expected_fragment}', but was '{self.driver.current_url}'"
            )
