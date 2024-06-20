from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds wait time

        # Wait for the username input to be present
        self.username_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        # Wait for the password input to be present
        self.password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        # Wait for the login button to be present
        self.login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

    def login(self, username, password):
        # Wait for the username input to be visible and enter username
        self.wait.until(EC.visibility_of(self.username_input)).send_keys(username)

        # Wait for the password input to be visible and enter password
        self.wait.until(EC.visibility_of(self.password_input)).send_keys(password)

        # Wait for the login button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
