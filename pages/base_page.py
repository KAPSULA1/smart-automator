from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def visit(self, url: str):
        self.driver.get(url)

    def find(self, by: By, locator: str):
        return self.driver.find_element(by, locator)

    def finds(self, by: By, locator: str):
        return self.driver.find_elements(by, locator)

    def click(self, by: By, locator: str):
        self.find(by, locator).click()

    def type(self, by: By, locator: str, text: str):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def exists(self, by: By, locator: str) -> bool:
        try:
            self.find(by, locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False
