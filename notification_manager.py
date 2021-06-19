from twilio.rest import Client
import smtplib
import os

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.environ.get('TWILIO_VERIFIED_NUMBER')
EMAIL_ID = os.environ.get('EMAIL_ID')
PASSWORD = os.environ.get('PASSWORD')
HOST = "smtp.gmail.com"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, email_id, msg):
        with smtplib.SMTP(HOST) as connection:
            connection.starttls()
            connection.login(EMAIL_ID, PASSWORD)
            connection.sendmail(EMAIL_ID, email_id, msg.encode('utf-8'))

