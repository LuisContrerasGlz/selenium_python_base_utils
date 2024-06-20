from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Function to set up the browser with the necessary configurations
def setup_browser():
    # Initialize the ChromeDriver service using WebDriverManager to handle driver binaries
    service = Service(ChromeDriverManager().install())
    
    # Create a new instance of the Chrome browser with the specified service
    driver = webdriver.Chrome(service=service)
    
    # Maximize the browser window for better visibility during tests
    driver.maximize_window()
    
    # Return the configured browser instance
    return driver

