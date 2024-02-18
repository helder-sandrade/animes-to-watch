from time import sleep
from .chrome.Chrome import Chrome
from random import randrange

class Rpa(Chrome):

    def __init__(self):
        self.driver = None
        super().__init__()

    def load_page(self, contador=0, tempo=0):
        self.start_driver()
        self.get_page_check(url='https://www.google.com.br')
        sleep(tempo)
        self.driver.save_screenshot(f'rpa/logs/google{contador}.png')
        self.shutdown()
