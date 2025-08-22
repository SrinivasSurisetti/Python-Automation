import time
import uuid
import smtplib
import ssl
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By

# -----------------------
# Function to generate random email
# -----------------------
def generate_unique_email():
    unique_id = uuid.uuid4().hex[:8]
    email = f"user{unique_id}@example.com"
    print("Generated Random Email:", email)
    return email

# -----------------------
# Selenium Part: Fill form with random email
# -----------------------
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")

unique_email = generate_unique_email()
email_input = driver.find_element(By.XPATH, "//input[@type='email']")
email_input.send_keys(unique_email)

time.sleep(5)  # keep short for demo, adjust if needed
driver.quit()

# -----------------------
# SMTP Part: Send the generated email to receiver
# -----------------------
subject = "Random Email Generated via Selenium"
body = f"The generated random email is: {unique_email}"

sender_email = "srinivassurisetti14@gmail.com"
receiver_email = "srinivassurisetti14@gmail.com"
password = input("Enter your Gmail App Password: ")  # Use app password, not your Gmail login

# Compose message
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h2>{subject}</h2>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

# Send email
context = ssl.create_default_context()
print("Sending Email...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email Sent Successfully!")
