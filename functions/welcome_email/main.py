
# Included Dependencies
# https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python37

# Deployment statement for command line...
# https://cloud.google.com/functions/docs/env-var
"""
gcloud functions deploy send_welcome_email --runtime python38 --trigger-event "providers/firebase.auth/eventTypes/user.create" --trigger-resource "datafaux-ab0de" --allow-unauthenticated --set-env-vars sendgridkey=LOOKATGOOGLECLOUDCONSOLETOGETSENDGRIDKEYFROM2021121
"""


import json
from setup_welcome_email import welcome_email


def send_welcome_email(data, context):
    """ Triggered by creation or deletion of a Firebase Auth user object.
     Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): Metadata for the event.
    """

    user_email = data["email"]
    print('Function triggered by creation/deletion of user: %s' % data["uid"])
    print('Created at: %s' % data["metadata"]["createdAt"])

    if 'email' in data:
        print('Email: %s' % data["email"])

    welcome_email('pupa.matt@gmail.com', user_email, 'Welcome to Datafaux!', 'Hello! We are happy to have you here!')
