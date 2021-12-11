
# https://github.com/sendgrid/sendgrid-python/blob/main/examples/helpers/mail_example.py#L9
# https://github.com/sendgrid/sendgrid-python/blob/HEAD/use_cases/attachment.md
# https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python

from google.cloud import functions
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import os


sendgrid_client = sendgrid.SendGridAPIClient(os.environ.get('sendgridkey', 'error'))

def welcome_email(sender, recipient, subject, content):

    message = Mail(from_email=sender
                    ,to_emails=recipient
                    ,subject=subject
                    ,plain_text_content=content
                    )

    try:
        response = sendgrid_client.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)
