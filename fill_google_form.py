from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_user_details():
    print("Please provide the following details:")
    details = {
        "full_name": input("Full Name: "),
        "contact_number": input("Contact Number (10 digits): "),
        "email_id": input("Email ID: "),
        "full_address": input("Full Address: "),
        "pin_code": input("Pin Code: "),
        "dob": input("Date of Birth (YYYY-MM-DD): "),
        "gender": input("Gender: ")
    }
    return details

# Get user details
user_details = get_user_details()

# Initialize WebDriver
driver = webdriver.Chrome()  
driver.get('https://forms.gle/WT68aV5UnPajeoSc8')  

try:
    # Fill Full Name
    full_name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full_name.send_keys(user_details["full_name"])

    # Fill Contact Number
    contact_number = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_number.send_keys(user_details["contact_number"])

    # Fill Email ID
    email_id = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id.send_keys(user_details["email_id"])

    # Fill Full Address
    full_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    full_address.send_keys(user_details["full_address"])

    # Fill Pin Code
    pin_code = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pin_code.send_keys(user_details["pin_code"])

    # Fill Date of Birth
    dob = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    dob.send_keys(user_details["dob"])

    # Fill Gender
    gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    gender.send_keys(user_details["gender"])

    # Read CAPTCHA code
    captcha_element = driver.find_element(By.XPATH, '//*[@id="i37"]/span[1]/b')  # XPath where the CAPTCHA code is displayed
    captcha_code = captcha_element.text

    # Fill CAPTCHA code
    captcha_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    captcha_input.send_keys(captcha_code)

    # Submit the Form
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    # Wait for submission confirmation
    time.sleep(3)

    # Capture a screenshot of the confirmation page
    driver.save_screenshot("form_submission_confirmation.png")
    print("Screenshot saved as 'form_submission_confirmation.png'.")

finally:
    # Close the WebDriver
    driver.quit()
