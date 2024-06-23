# Selenium with Python and Pytest base utils

Base utils for re-use code for Selenium with python, such as hovers, waits, imports, basic POM structure, login examples.

## Installation Requirements

Before you start running the project, ensure that you have the following software installed on your system:

1. Python
    This project is built on Python, so make sure you have it installed. The recommended version is Python 3.8 or later.
    [Download Python](https://www.python.org/downloads/).
    
2. Pytest
    Pytest is used for running automated tests in this project. Install it via pip:

    - pip install pytest

3. Allure Report
    Allure is a reporting tool that generates test reports from Pytest results. To install Allure:

    - pip install allure-pytest

4. Request Module for API Requests
    To interact with APIs, we use the requests library. You can install it with:

    - pip install requests

5. Node.js
    You can download and install it from the official site:

    [Download Node.js](https://nodejs.org/).

6. Allure command-line
    In terminal run the following command: 
    - npm install -g allure-commandline
    - allure - options

To run test you can use pytest command or to specify the browser: pytest -m sandbox --browser chrome

To run and get Allure report you can use: 
pytest -m sandbox --browser chrome --alluredir alure-results

Then to open report: 
allure serve allure_results

In this repo you can see an example in the folder

