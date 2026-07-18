from utils.driver_factory import create_driver
from features.pages.login_page import LoginPage
from features.pages.transfer_page import TransferPage
from config.settings import BASE_URL
from selenium.webdriver.common.by import By
import time

driver = create_driver(headless=False)
try:
    driver.get(BASE_URL)
    login_page = LoginPage(driver, BASE_URL)
    login_page.login('userauto123', 'senha123')
    time.sleep(2)
    transfer_page = TransferPage(driver, BASE_URL)
    transfer_page.open_transfer_page()
    time.sleep(2)
    html = driver.page_source
    print('URL:', driver.current_url)
    print('Page title:', driver.title)
    print('HTML length:', len(html))
    tokens = ['fromAccountId', 'toAccountId', 'amount', 'Transfer Funds', 'name="fromAccountId"', 'name="toAccountId"', 'id="amount"', 'value="Transfer"', 'select name="fromAccountId"']
    for token in tokens:
        print(f"{token}: {html.count(token)}")
        idx = html.find(token)
        if idx != -1:
            snippet = html[max(idx - 200, 0):min(idx + 200, len(html))]
            print('SNIPPET:', snippet.replace('\n', ' ').replace('    ', ' ')[:400])
    print('--- inputs ---')
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input, select, textarea')
    print('total form elements:', len(inputs))
    for i, elem in enumerate(inputs[:20], start=1):
        print(i, elem.tag_name, elem.get_attribute('name'), elem.get_attribute('id'), elem.get_attribute('type'), elem.get_attribute('outerHTML')[:120])
    print('--- forms ---')
    forms = driver.find_elements(By.CSS_SELECTOR, 'form')
    print('forms count:', len(forms))
    for i, form in enumerate(forms, start=1):
        print('form', i, form.get_attribute('action'), 'inputs:', len(form.find_elements(By.CSS_SELECTOR, 'input, select, textarea')))
        print(form.get_attribute('outerHTML')[:400].replace('\n', ' '))
finally:
    driver.quit()
