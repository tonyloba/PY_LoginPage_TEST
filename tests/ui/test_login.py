from pages.login_page import LoginPage
from utils.config import load_config
from utils.waits import wait_for_visible


def test_valid_login(driver):
    config = load_config()
    driver.get(config["url"])

    login_page = LoginPage(driver)
    login_page.login(config["valid_user"], config["valid_pass"])

    assert "/logged-in-successfully"
def test_invalid_login(driver):
    config = load_config()
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(config["valid_user"], "wrong_password")

    assert login_page.get_error_message() == "Your password is invalid!"

def test_negative_login(driver):
    config = load_config()
    driver.get(config["url"])

    login_page = LoginPage(driver)
    login_page.login(config["user"], config["12345"])