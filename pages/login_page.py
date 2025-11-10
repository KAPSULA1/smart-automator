import os
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT   = (By.CSS_SELECTOR, "button.radius")
    FLASH    = (By.ID, "flash")

    def open(self):
        base = os.getenv("BASE_URL").rstrip("/")
        path = os.getenv("LOGIN_PATH", "/login")
        self.visit(base + path)

    def login(self, user: str, pwd: str):
        self.type(*self.USERNAME, text=user)
        self.type(*self.PASSWORD, text=pwd)
        self.click(*self.SUBMIT)

    def success_message(self) -> str:
        return self.find(*self.FLASH).text.strip()
