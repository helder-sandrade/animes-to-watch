import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

CHROME = r'/app/selenium/driver/chromedriver'
LOGS_DIR = r'/app/selenium/logs/imagens/'

with Display(size=(2048, 1080)) as dsp:
    options = Options()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(executable_path=CHROME), options=options)
    driver.maximize_window()
    driver.get(url='https://www.google.com')
    sleep(3)
    driver.save_screenshot(filename=os.path.join(LOGS_DIR, 'google.png'))
    driver.quit()

