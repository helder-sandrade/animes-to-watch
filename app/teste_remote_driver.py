from threading import Thread
from time import sleep
from selenium import webdriver


def roda_webdriver(i=0):
    try:
        option = webdriver.ChromeOptions()
        option.add_argument('--window-size=1920,1080')
        driver = webdriver.Remote(command_executor='http://hub-animes-to-watch:4444', options=option)
        print(driver)
        # driver.get('https://172.19.0.4:5555')
        driver.get('https://google.com/')
        print(f'{i} : http://hub-animes-to-watch:4444')
        driver.save_screenshot(filename=f'/app/rpa/logs/imagens/tela_google0{i}.png')
        sleep(20)
        driver.quit()
    except Exception as e:
        print(e)


for i in range(6):
    thread = Thread(target=roda_webdriver, args=(i,))
    thread.start()
    print(f'Iniciando a thread: {i}')
