import pytest

from pages.login_page import LoginPage
from utils.browser_setup import setup_browser


@pytest.fixture
def browser():
    driver = setup_browser()
    yield driver
    driver.quit()

def test_valid_login(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(browser)
    login_page.login("Admin", "admin123")
    assert "OrangeHRM" in browser.title
