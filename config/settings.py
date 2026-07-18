import os

BASE_URL = os.getenv("PARABANK_URL", "https://parabank.parasoft.com/parabank")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
REPORTS_DIR = os.path.join(os.getcwd(), "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
ALLURE_RESULTS_DIR = os.path.join(REPORTS_DIR, "allure-results")
