from pages.login_page import LoginPage
from utils.config import load_config, load_csv
from utils.waits import wait_for_visible


def test_valid_login(driver):
    config = load_config()
    driver.get(config["url"])

    login_page = LoginPage(driver)
    login_page.login(config["valid_user"], config["valid_pass"])

    assert "/logged-in-successfully" in driver.current_url
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

def test_valid_login_csv(driver):
    test_data = load_csv()
    driver.get(test_data["url"])
    login_page = LoginPage(driver)
    login_page.login(test_data["username"], test_data["password"])
    assert "/logged-in-successfully" in driver.current_url

def test_invalid_login_csv(driver):
    test_data = load_csv()
    driver.get(test_data["url"])
    login_page = LoginPage(driver)
    login_page.login(test_data["username"], "wrong_password")
    assert "Your password is invalid!" in login_page.get_error_message()

def test_negative_login_csv(driver):
    test_data = load_csv()
    driver.get(test_data["url"])
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")
    assert "Your username is invalid!" in login_page.get_error_message()