import os
import re

from config.settings import BASE_URL, SCREENSHOTS_DIR
from utils.driver_factory import create_driver
from utils.helpers import logger, take_screenshot


def before_all(context):
    context.base_url = BASE_URL
    context.reports_dir = SCREENSHOTS_DIR
    os.makedirs(context.reports_dir, exist_ok=True)
    logger.info("Configuração inicial concluída para execução Behave")


def before_scenario(context, scenario):
    headless = os.getenv("HEADLESS", "false").lower() == "true" or os.getenv("CI") is not None
    context.driver = create_driver(headless=headless)
    context.scenario_name = sanitize_name(scenario.name)
    logger.info(f"Iniciando cenário: {scenario.name} (headless={headless})")


def after_step(context, step):
    if step.status == "failed" and hasattr(context, "driver"):
        screenshot_path = take_screenshot(context.driver, context.reports_dir, context.scenario_name, step.name)
        context.last_screenshot = screenshot_path
        logger.error(f"Falha no step '{step.name}'. Screenshot salvo em: {screenshot_path}")


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
        logger.info(f"Cenário finalizado: {scenario.name}")


def sanitize_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", value)
