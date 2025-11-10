import os
from dotenv import load_dotenv
from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success():
    load_dotenv()
    driver = create_driver()
    try:
        login = LoginPage(driver)
        login.open()
        login.login(os.getenv("DEMO_USER"), os.getenv("DEMO_PASS"))
        msg = login.success_message()
        assert "You logged into a secure area!" in msg
    finally:
        driver.quit()
