import time

from selenium import webdriver

from selenium.webdriver.common.by import By

import uuid

def generate_unique_email(): 

    unique_id=uuid.uuid4().hex[:8]

    email =f"user{unique_id}@example.com"

    print(email)

    return email

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Register.html")

unique_email=generate_unique_email()

email_input=driver.find_element(By.XPATH, "//input[@type='email']")

email_input.send_keys(unique_email)

time.sleep(20)


driver.quit()