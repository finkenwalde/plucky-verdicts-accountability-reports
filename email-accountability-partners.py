import os
import smtplib
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email
EMAIL_PASSWORD = "your_password"  # Replace with your email password
RECIPIENT_EMAILS = ["partner1@example.com", "partner2@example.com"]  # List of accountability partner emails

# Path to the report file
current_directory = os.path.dirname(os.path.realpath(__file__))
report_file_path = os.path.join(current_directory, "accountability-report.txt")

# Function to send an email with the report to all recipients
def send_email():
    try:
        with open(report_file_path, 'r') as report_file:
            report_content = report_file.read()

        msg = MIMEText(report_content)
        msg['Subject'] = 'Accountability Report'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ', '.join(RECIPIENT_EMAILS)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # For Gmail
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully to:", ', '.join(RECIPIENT_EMAILS))
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to schedule the email
def schedule_email(schedule_time, frequency):
    if frequency == 'daily':
        schedule.every().day.at(schedule_time).do(send_email)
    elif frequency == 'weekly':
        schedule.every().week.at(schedule_time).do(send_email)
    else:
        print("Unsupported frequency. Please use 'daily' or 'weekly'.")

if __name__ == "__main__":
    # Set your desired schedule time and frequency here
    SCHEDULE_TIME = "09:00"  # Change to desired time (24-hour format)
    FREQUENCY = "daily"  # Change to 'weekly' if needed

    schedule_email(SCHEDULE_TIME, FREQUENCY)

    print(f"Scheduled email to be sent {FREQUENCY} at {SCHEDULE_TIME}.")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
