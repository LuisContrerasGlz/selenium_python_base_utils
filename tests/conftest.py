import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.sandbox_page import SandboxPage


# Function to add custom command line options to pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser: chrome, firefox, edge, safari",
    )

# Fixture to set up the browser instance based on the command line option
@pytest.fixture(scope="session")
def browser(request):
    # Get the browser type from command line options
    browser_type = request.config.getoption("--browser").lower()
    
    # Set up the browser driver based on the browser type
    if browser_type == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_type == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser_type == "safari":
        driver = webdriver.Safari()
    else:
        # Raise an error if the browser type is not supported
        raise ValueError(f"Browser {browser_type} not supported")

    # Provide the WebDriver instance to the test and ensure cleanup
    yield driver
    driver.quit()

# Fixture to provide an instance of the SandboxPage
@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)
