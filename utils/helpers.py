import logging
import os
import re
from datetime import datetime
from pathlib import Path

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestLogger:
    def __init__(self, name="parabank-tests"):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


logger = TestLogger()


def sanitize_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", value)


def ensure_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def take_screenshot(driver, output_dir, scenario_name, step_name):
    ensure_directory(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{sanitize_name(scenario_name)}_{sanitize_name(step_name)}_{timestamp}.png"
    screenshot_path = os.path.join(output_dir, file_name)
    driver.save_screenshot(screenshot_path)
    return screenshot_path


def click_element(driver, locator, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()
    return element


def fill_field(driver, locator, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(value)
    return element


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def get_text(driver, locator, timeout=10):
    return wait_for_element(driver, locator, timeout).text


def validate_text(driver, locator, expected_text, timeout=10):
    actual_text = get_text(driver, locator, timeout)
    if expected_text not in actual_text:
        raise AssertionError(f"Expected text '{expected_text}' not found. Actual text: '{actual_text}'")


def validate_url(driver, expected_fragment):
    if expected_fragment not in driver.current_url:
        raise AssertionError(f"Expected URL to contain '{expected_fragment}', but was '{driver.current_url}'")


def get_element_or_none(driver, locator, timeout=10):
    try:
        return wait_for_element(driver, locator, timeout)
    except (NoSuchElementException, TimeoutException):
        return None
