import os
import shutil
import platform
import logging
import traceback
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f':::Iniciando o script de download do chromedriver:::"')
path_script = os.path.dirname(os.path.abspath(__file__))
driver_dir = os.path.join(path_script, 'driver')

chromedriver = 'chromedriver'
print(f"Plataforma encontrada: '{platform.system()}'")
if 'Windows' in platform.system():
    chromedriver = 'chromedriver.exe'

path_chromedriver = os.path.join(driver_dir, chromedriver)
if os.path.isfile(path_chromedriver):
    logging.info(f'Driver já existe na pasta : "{path_chromedriver}"')
else:
    try:
        CHROME = ChromeDriverManager().install()
        logging.info(f'Baixado o driver: "{CHROME}"')
        shutil.move(src=CHROME, dst=path_chromedriver)
        logging.info(f'Movido para a pasta: "{path_chromedriver}"')
    except Exception:
        logging.error(f'Não foi possivel baixar o driver')
        logging.error(traceback.print_exc())

print("Fim do download do driver")