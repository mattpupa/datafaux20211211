
# https://github.com/sendgrid/sendgrid-python/blob/main/examples/helpers/mail_example.py#L9
# https://github.com/sendgrid/sendgrid-python/blob/HEAD/use_cases/attachment.md
# https://www.twilio.com/blog/sending-email-attachments-with-twilio-sendgrid-python

from google.cloud import functions
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import base64
import os

sendgrid_client = sendgrid.SendGridAPIClient(os.environ.get('sendgridkey', 'error'))

def send_email(sender, recipient, subject, content, file_to_attach):

    message = Mail(from_email=sender
                    ,to_emails=recipient
                    ,subject=subject
                    ,plain_text_content=content
                    )

    file_path = file_to_attach
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()

    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/csv')
    attachment.file_name = FileName(file_path.lstrip(("/tmp/")))
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment

    try:
        response = sendgrid_client.send(message)
        os.remove(file_path) # https://www.w3schools.com/python/python_file_remove.asp
        print(response.status_code)
    except Exception as e:
        print(e.message)
