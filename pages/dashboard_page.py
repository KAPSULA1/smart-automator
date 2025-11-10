from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    # the-internet.herokuapp.com-ზე წარმატებული ლოგინის შემდეგ კვლავ ამავე გვერდზე ჩანს flash
    HEADER = (By.TAG_NAME, "h2")

    def heading(self) -> str:
        els = self.finds(*self.HEADER)
        return els[0].text if els else "Dashboard"
