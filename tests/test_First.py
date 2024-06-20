import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
def test_test_google():
    driver.get("https://www.google.com/")
    title_page_google = driver.title
    assert title_page_google == "Google"

def test_test_amazon():
    driver.get("https://www.amazon.com/")
    title_page_amazon = driver.title
    assert title_page_amazon == "Amazon.com en espanol. Gasta menos. Sonríe más."