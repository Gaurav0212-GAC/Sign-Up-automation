# Signup Automation Project

## Overview

This project contains test cases and Selenium automation scripts for testing the sign-up and sign-in flows on the Magento website. The project is designed to verify the following:

- Navigation to the sign-up page
- Successful account creation with valid data
- Successful sign-in with registered account
- Error handling for attempting to sign up with an existing email
- Validation of invalid email formats during sign-up

## Files Included

- *Signup_Automation_Test_Cases.xlsx*: A document containing detailed test cases for the sign-up and sign-in flows.
- *signup_automation_script.py*: A Selenium automation script written in Python that automates the sign-up and sign-in process on the Magento website.

## Setup and Execution

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium WebDriver](https://www.selenium.dev/)
- A browser driver like [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Chrome or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox.

### Installing Dependencies

1. Install Selenium using pip:
    bash
    pip install selenium
    

2. Ensure that the browser driver (e.g., ChromeDriver) is in your PATH or specify the driver’s location in the script.

### Running the Automation Script

1. Open a terminal and navigate to the directory containing the signup_automation_script.py file.
2. Run the script using Python:
    bash
    python signup_automation_script.py
    

The script will automate the process of signing up a new user and then signing in with that user on the Magento website.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.
