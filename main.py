import os
from dotenv import load_dotenv
from utils.logger import log_step, log_info, log_error
from utils.driver_factory import create_driver
from utils.data_exporter import export_csv
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from tabulate import tabulate

def run_demo():
    load_dotenv()
    driver = None
    rows = []

    try:
        log_step("Launching browser")
        driver = create_driver()

        log_step("Opening Login Page")
        login = LoginPage(driver)
        login.open()

        user = os.getenv("DEMO_USER")
        pwd  = os.getenv("DEMO_PASS")

        log_step("Submitting credentials")
        login.login(user, pwd)

        log_step("Verifying success & collecting data")
        msg = login.success_message()
        dash = DashboardPage(driver)
        heading = dash.heading()

        row = {
            "status": "OK" if "You logged into a secure area!" in msg else "CHECK",
            "flash": msg.split("\n")[0],
            "page_heading": heading
        }
        rows.append(row)
        log_info("Data captured")

        log_step("Exporting CSV")
        out = export_csv(rows)
        log_info(f"Exported: {out}")

        print("\n" + tabulate(rows, headers="keys", tablefmt="github"))
    except Exception as e:
        log_error(f"Unhandled error: {e}")
        raise
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    run_demo()
