
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (assuming Chrome is used)
driver = webdriver.Chrome()

# Test Case 1: Navigate to Sign Up Page
driver.get("https://magento.softwaretestingboard.com/")
driver.find_element(By.LINK_TEXT, "Create an Account").click()

# Test Case 2: Fill in Sign Up Form with Valid Data
driver.find_element(By.ID, "firstname").send_keys("John")
driver.find_element(By.ID, "lastname").send_keys("Doe")
driver.find_element(By.ID, "email_address").send_keys("johndoe@example.com")
driver.find_element(By.ID, "password").send_keys("SecurePass123")
driver.find_element(By.ID, "password-confirmation").send_keys("SecurePass123")
driver.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()

# Test Case 3: Sign In with Registered Account
driver.find_element(By.LINK_TEXT, "Sign Out").click()
driver.find_element(By.LINK_TEXT, "Sign In").click()
driver.find_element(By.ID, "email").send_keys("johndoe@example.com")
driver.find_element(By.ID, "pass").send_keys("SecurePass123")
driver.find_element(By.ID, "send2").click()


# Tear down the WebDriver
driver.quit()

# script is created by gaurav singh gaurav.singh020499@gmail.com 
