"""
Interface file for implementing chromedriver.
Created by: Helder dos Santos Andrade
"""
from typing import Optional, Union
from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class Chrome:
    def __init__(self): ...

    def start_driver(self, timeout: Optional[int]) -> bool: ...

    def shutdown(self) -> None: ...

    def get_page_check(self, url: str, timer: Optional[int]) -> bool: ...

    def get_state_complete(self, count: Optional[int]) -> bool: ...

    def set_text_by_send_keys(self, xpath: str, text: str, timer: Optional[int]) -> None: ...

    def set_text_by_script(self, xpath: str, text: str, timer: Optional[int]) -> None: ...

    def get_text_value(self, xpath: str, timer: Optional[int]) -> str: ...

    def get_text_by_attribute(self, xpath: str, attribute: str, timer: Optional[int]) -> str: ...

    def click_by_script(self, xpath: str, timer: Optional[int]) -> None: ...

    def dbl_click_by_script(self, xpath: str, timer: Optional[int]) -> None: ...

    def click_element(self, xpath: str, timer: Optional[int]) -> None: ...

    def click_perform(self, xpath: str, timer: Optional[int]) -> None: ...

    def dbl_click_perform(self, xpath: str, timer: Optional[int]) -> None: ...

    def move_perform(self, xpath: str, timer: Optional[int]) -> None: ...

    def select_by_text(self, xpath: str, text: str, timer: Optional[int]) -> None: ...

    def get_text_by_select(self, xpath: str, timer: Optional[int]) -> str: ...

    def select_by_similarity(self, xpath: str, text: str, timer: Optional[int], choice_count: Optional[int]) -> None: ...

    def invisibility_element(self, xpath: str, timer: Optional[int]) -> bool: ...

    def presence_element(self, xpath: str, timer: Optional[int]) -> bool: ...

    def find_iframe(self, xpath: str) -> bool: ...

    def get_html_element(self, xpath: str, timer: Optional[int]) -> BeautifulSoup: ...

    def scroll_to_element(self, xpath: str, timer: Optional[int]) -> bool: ...
