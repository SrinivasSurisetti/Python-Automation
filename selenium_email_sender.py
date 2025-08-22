from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -------------------------------
# STEP 1: Configure Chrome options
# -------------------------------
options = webdriver.ChromeOptions()

# Replace with your actual Chrome user profile path
# For Windows (example):
options.add_argument(r"user-data-dir=C:\Users\YOUR_USERNAME\AppData\Local\Google\Chrome\User Data")

# -------------------------------
# STEP 2: Start Chrome with profile
# -------------------------------
driver = webdriver.Chrome(options=options)
driver.get("https://mail.google.com/")

time.sleep(5)  # wait for Gmail to load

# -------------------------------
# STEP 3: Compose and send email
# -------------------------------
driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3").click()  # Compose button
time.sleep(2)

# Receiver email
driver.find_element(By.NAME, "to").send_keys("receiver_email@gmail.com")

# Subject
driver.find_element(By.NAME, "subjectbox").send_keys("Test Email from Selenium")

# Body
driver.find_element(By.CSS_SELECTOR, "div[aria-label='Message Body']").send_keys(
    "Hello,\n\nThis is an automated email sent using Selenium!\n\n- Python Bot"
)

# Click Send
driver.find_element(By.CSS_SELECTOR, "div[data-tooltip='Send ‪(Ctrl-Enter)‬']").click()

print("✅ Email Sent Successfully!")
time.sleep(5)

# Close browser
driver.quit()
