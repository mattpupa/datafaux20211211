

# Included Dependencies
# https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python37

# Deployment statement for command line...
# https://cloud.google.com/functions/docs/env-var
"""
gcloud functions deploy query_bigquery --runtime python38 --trigger-event "providers/cloud.firestore/eventTypes/document.create" --trigger-resource "projects/datafaux-ab0de/databases/(default)/documents/datasetRequests/{documentID}" --allow-unauthenticated --timeout=540 --set-env-vars sendgridkey=LOOKATGOOGLECLOUDCONSOLEFORSENDGRIDKEY20211211 --memory=256
"""

from setup_sendgrid import send_email
from create_records import create_fields, create_columns
import pandas


def query_bigquery(data, context):

    # get eventID for csv file name
    eventID = context.event_id

    # Get dictionary object that was entered into firestore
    fields_requested = data["value"]["fields"]

    userEmail = data["value"]["fields"]["currentUserEmail"]["stringValue"]

    # Create variable for number of rows in the dataframe ...FIGURE THIS OUT!
    number_of_rows = 1000

    email_text = """
                 Here's your Datafaux file with the fields requested.

                 If you want to be emailed when Datafaux officially launches,
                 just reply to this email. If you have any suggestions for features
                 or other data fields you'd like to see available in Datafaux, please
                 share those as well!

                 Matt
                """


    # Create dataframe from records
    # https://stackoverflow.com/questions/4112265/how-to-zip-lists-in-a-list
    df = pandas.DataFrame(list(zip(*create_fields(fields_requested, number_of_rows))), columns=create_columns(fields_requested))

    # Use /tmp for writable file!
    # https://cloud.google.com/functions/docs/concepts/exec#file_system
    df.to_csv(f'/tmp/{eventID}.csv', index=False)

    del df

    print(context)
    print(data)

    send_email('pupa.matt@gmail.com'
                , userEmail
                , 'Datafaux data set file'
                , email_text
                , f'/tmp/{eventID}.csv'
                )


    # https://sendgrid.com/

# https://docs.python.org/3/library/io.html
# https://cmdlinetips.com/2020/05/how-to-save-pandas-dataframe-as-gzip-zip-file/
