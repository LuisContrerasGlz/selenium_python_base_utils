from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class BasePage:
    def __init__(self, driver):
        # Initialize the BasePage with the WebDriver instance
        self.driver = driver

    def navigate_to(self, url):
        # Navigate to the specified URL
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        # Wait for an element to be visible on the page within the given timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        # Click on the element located by the specified locator
        self.wait_for_element(locator).click()

    def type_text(self, locator, text):
        # Find the element, clear any existing text, and type the specified text
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_visible_text(self, locator, text):
        # Select an option from a dropdown menu by visible text
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, index):
        # Select an option from a dropdown menu by index
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)

    def get_select_options(self, locator):
        # Get all options from a dropdown menu as a list of text values
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def select_element(self, locator):
        # Select a checkbox or radio button if it is not already selected
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def unselect_checkbox(self, locator):
        # Unselect a checkbox if it is currently selected
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def hover_over_element(self, locator):
        # Hover the mouse over the element located by the specified locator
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def reload_page(self):
        # Refresh the current page
        self.driver.refresh()
