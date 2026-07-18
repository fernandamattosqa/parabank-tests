import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.settings import DEFAULT_TIMEOUT, HEADLESS


def create_driver(headless=False):
    options = Options()
    if headless or HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.default_content_setting_values.popups": 2,
        "credentials_enable_service": False,
    })

    chrome_driver_path = os.getenv("CHROMEDRIVER_PATH")
    if chrome_driver_path:
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    else:
        driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    return driver
