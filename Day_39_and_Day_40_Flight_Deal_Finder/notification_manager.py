from twilio.rest import Client
from smtplib import SMTP


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, Twilio_Account_Sid, Twilio_Auth_Token, Twilio_SMS_Number, Twilio_Whatsapp_Number,
                 Twilio_Verified_Number, SMTP_Address, Email, App_Password):
        self.account_sid = Twilio_Account_Sid
        self.auth_token = Twilio_Auth_Token
        self.sms_number = Twilio_SMS_Number
        self.whatsapp_number = Twilio_Whatsapp_Number
        self.verified_number = Twilio_Verified_Number
        self.client = Client(self.account_sid, self.auth_token)
        self.smtp_address = SMTP_Address
        self.email = Email
        self.app_password = App_Password

    def send_sms(self, message_body):
        # Method 1 - SMS
        message = self.client.messages.create(
            body=message_body,
            from_=self.sms_number,
            to=self.verified_number,
        )
        print(message.status)

    def send_whatsapp_sms(self, message_body):
        # Method 2 - Whatsapp message
        message = self.client.messages.create(
            body=message_body,
            from_=f"whatsapp:{self.whatsapp_number}",
            to=f"whatsapp:{self.verified_number}",
        )
        print(message.status)

    def send_emails(self, customer_email_list, message_body):
        with SMTP(self.smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.app_password)

            for email in customer_email_list:
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message_body}".encode('utf-8')
                )

