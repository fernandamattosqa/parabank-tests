from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless=new')
options.add_argument('--window-size=1200,800')
driver = webdriver.Chrome(options=options)
try:
    driver.get('https://parabank.parasoft.com/parabank/')
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    print('total anchors:', len(anchors))
    for a in anchors:
        text = a.text.strip()
        href = a.get_attribute('href')
        if 'Transfer' in text or (href and 'transfer' in href.lower()):
            print('MATCH:', repr(text), href)
    print('\nFirst 20 anchors:')
    for i, a in enumerate(anchors[:20]):
        print(i + 1, repr(a.text.strip()), a.get_attribute('href'))
finally:
    driver.quit()
