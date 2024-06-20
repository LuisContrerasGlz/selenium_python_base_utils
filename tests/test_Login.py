import pytest

from pages.login_page import LoginPage
from utils.browser_setup import setup_browser


# Fixture to set up and tear down the browser for each test
@pytest.fixture
def browser():
    # Initialize the browser using a custom setup function
    driver = setup_browser()
    # Provide the driver to the test
    yield driver
    # Quit the browser after the test is done
    driver.quit()

# Test function to verify valid login functionality
def test_valid_login(browser):
    # Navigate to the login page of the application
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Initialize the LoginPage object with the browser instance
    login_page = LoginPage(browser)
    
    # Perform login action with valid credentials
    login_page.login("Admin", "admin123")
    
    # Assert that the login was successful by checking the page title
    assert "OrangeHRM" in browser.title
