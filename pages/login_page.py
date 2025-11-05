from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.USERNAME = (By.ID, "username")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.XPATH, "//button[text()='Submit']")
        self.ERROR_MSG = (By.ID, "error")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text