from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("student")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Password123")

submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

assert "/logged-in-successfully" in driver.current_url
