import os
import re
from selenium import webdriver

from config.settings import BASE_URL, SCREENSHOTS_DIR
from utils.helpers import logger, take_screenshot


def before_all(context):
    context.base_url = BASE_URL
    context.reports_dir = SCREENSHOTS_DIR
    os.makedirs(context.reports_dir, exist_ok=True)
    logger.info("Configuração inicial concluída para execução Behave")


def before_scenario(context, scenario):
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")

        # Desativa prompts e abre em modo limpo
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")

        context.driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--inprivate")

        context.driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Navegador não suportado: {browser}")

    context.driver.maximize_window()
    context.scenario_name = sanitize_name(scenario.name)
    logger.info(f"Iniciando cenário: {scenario.name} (browser={browser}, headless={headless})")


def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        screenshot_path = take_screenshot(
            context.driver,
            context.reports_dir,
            context.scenario_name,
            step.name
        )
        context.last_screenshot = screenshot_path
        logger.error(f"Falha no step '{step.name}'. Screenshot salvo em: {screenshot_path}")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
        logger.info(f"Cenário finalizado: {scenario.name}")


def sanitize_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", value)
