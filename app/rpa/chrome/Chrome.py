import os
import re
from time import sleep
from bs4 import BeautifulSoup
from typing import Optional
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


class Chrome:

    def __init__(self) -> None:
        """
        # Start Chrome Class
        """
        self.driver = None
        self.wait = None
        self.action = None
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.accept_untrusted_certs = True
        self.chrome_options.assume_untrusted_cert_issuer = True
        self.chrome_options.add_argument("--enable-javascript")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--safebrowsing-disable-download-protection")
        self.chrome_options.add_argument("--window-size=1920,1080")

        # preferences = {
        #    "download.default_directory": os.path.join(os.getcwd(), self.app, "downloads"),
        #    "download.prompt_for_download": False,
        #    "profile.default_content_setting_values.automatic_downloads": 1,
        #    "safebrowsing.enabled": True,
        # }
        # self.download_dir = os.path.join(os.getcwd(), self.app, "downloads")
        # self.chrome_options.add_experimental_option('prefs', preferences)

    def start_driver(self, timeout: Optional[int] = 10) -> bool:
        """
        # starts the remote driver if running docker or the local driver if running locally
        """
        try:
            if settings.LOCAL_DRIVER:
                self.driver = webdriver.Chrome(
                    service=Service(
                        executable_path=os.path.join(os.getcwd(), "rpa", "driver", "chromedriver.exe")),
                    options=self.chrome_options)
            else:
                self.driver = webdriver.Remote(
                    command_executor='http://hub-animes-to-watch:4444',
                    options=self.chrome_options
                )
            self.driver.maximize_window()
            self.wait = WebDriverWait(driver=self.driver, timeout=timeout)
            self.action = ActionChains(driver=self.driver)
            return True
        except WebDriverException:
            return False
        except Exception:
            return False

    def shutdown(self) -> None:
        """
        # chromedriver close function
        """
        self.driver.quit()
        del self.driver

    def get_page_check(self, url: str, timer: Optional[int] = 30) -> bool:
        """
        # open a new url and check if it loaded completely
        """
        self.driver.set_page_load_timeout(timer)
        self.driver.get(url)
        return self.get_state_complete()

    def get_state_complete(self, count: Optional[int] = 20) -> bool:
        """
        # script check if the page has fully loaded
        """
        try:
            state = None
            for i in range(count):
                state = str(self.driver.execute_script('return document.readyState'))
                if state == 'complete':
                    return True
                sleep(0.5)
            return False
        except Exception:
            pass

    def set_text_by_send_keys(self, xpath: str, text: str, timer: Optional[int] = 10) -> None:
        """
        # assign a text by typing
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        element.clear()
        element.send_keys(text)

    def set_text_by_script(self, xpath: str, text: str, timer: Optional[int] = 10) -> None:
        """
        # assign a text by script
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        element.clear()
        self.driver.execute_script(f"arguments[0].value = '{text}'", element)

    def get_text_value(self, xpath: str, timer: Optional[int] = 10) -> str:
        """
        # get the text assigned to an element
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        return element.text

    def get_text_by_attribute(self, xpath: str, attribute: str, timer: Optional[int] = 10) -> str:
        """
        # get the text of an attribute of the element
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        return element.get_attribute(attribute)

    def click_by_script(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # execute click by script
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def dbl_click_by_script(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # execute double click by script
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        self.driver.execute_script("arguments[0].ondblclick()", element)

    def click_element(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # execute click in element
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        element.click()

    def click_perform(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # execute click with movement
        """
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        action.move_to_element(element)
        action.perform()
        element.click()

    def dbl_click_perform(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # execute double click with movement
        """
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        action.move_to_element(element)
        action.perform()
        action.double_click(element)
        action.perform()

    def move_perform(self, xpath: str, timer: Optional[int] = 10) -> None:
        """
        # move mouse to element
        """
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        action.move_to_element(element)
        action.perform()

    def select_by_text(self, xpath: str, text: str, timer: Optional[int] = 10) -> None:
        """
        # select object by full text
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        select_element = Select(element)
        select_element.select_by_visible_text(text)

    def get_text_by_select(self, xpath: str, timer: Optional[int] = 10) -> str:
        """
        # returns the selected option from a checkbox
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        select_element = Select(element)
        return select_element.first_selected_option.text

    def select_by_similarity(self, xpath: str, text: str, timer: Optional[int] = 10,
                             choice_count: Optional[int] = 2000) -> None:
        """
        # select the object by similarity in the text
        """
        count = 0
        choices = []
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
        wait.until(ec.element_to_be_clickable((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        select_element = Select(element)

        for i in select_element.options:
            if count == choice_count:
                break
            choices.append(i.text)
            count += 1

        pattern = re.compile(text, re.IGNORECASE)

        for choice in choices:
            if pattern.search(choice):
                select_element.select_by_visible_text(choice)

    def invisibility_element(self, xpath: str, timer: Optional[int] = 10) -> bool:
        """
        # check if a visible object has become invisible
        """
        try:
            wait = WebDriverWait(self.driver, timer)
            wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
            wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
            wait.until(ec.invisibility_of_element((by.XPATH, xpath)))
            sleep(1)
            return True
        except Exception:
            return False

    def presence_element(self, xpath: str, timer: Optional[int] = 10) -> bool:
        """
        # check a visibility of object
        """
        try:
            wait = WebDriverWait(self.driver, timer)
            wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
            wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
            return True
        except Exception:
            return False

    def find_iframe(self, xpath: str) -> bool:
        """
        # check for the presence of an element in an iframes structure
        """
        retorno = False
        iframes = self.driver.find_elements(by.TAG_NAME, 'iframe')
        for i in range(len(iframes)):
            if retorno:
                break
            self.driver.switch_to.frame(i)
            try:
                wait = WebDriverWait(self.driver, 1)
                wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
                retorno = True
            except (NoSuchElementException, TimeoutException):
                pass
            interno = self.driver.find_elements(by.TAG_NAME, 'iframe')
            if len(interno) > 0:
                retorno = self.find_iframe(xpath)
            if not retorno:
                self.driver.switch_to.parent_frame()
        return retorno

    def get_html_element(self, xpath: str, timer: Optional[int] = 10) -> BeautifulSoup:
        """
        # returns the html of the selected element
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        html = element.get_attribute('innerHTML')
        return BeautifulSoup(html, "html.parser")

    def scroll_to_element(self, xpath: str, timer: Optional[int] = 10) -> bool:
        """
        # scroll the page until the element is visible
        """
        wait = WebDriverWait(self.driver, timer)
        wait.until(ec.presence_of_element_located((by.XPATH, xpath)))
        element = self.driver.find_element(by.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        try:
            wait.until(ec.visibility_of_element_located((by.XPATH, xpath)))
            return True
        except Exception:
            return False
