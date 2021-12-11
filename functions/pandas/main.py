
# Included Dependencies
# https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python37

# Deployment statement for command line...
# https://cloud.google.com/functions/docs/env-var
"""
gcloud functions deploy send_to_pandas --runtime python38 --trigger-event "providers/cloud.firestore/eventTypes/document.create" --trigger-resource "projects/datafaux-ab0de/databases/(default)/documents/datasetRequests/{documentID}" --allow-unauthenticated --timeout=540 --set-env-vars sendgridkey=LOOKATGOOGLECLOUDCONSOLETOGETSENDGRIDKEY20211211 --memory=256
"""


from google.cloud import firestore
import pandas
# import numpy
import faker
# import anonymizedf
#from populate_functions import populate_name, populate_address, populate_id, populate_company, populate_date, populate_username, populate_email
from setup_sendgrid import send_email
from create_columns import create_fields

db = firestore.Client()

def send_to_pandas(data, context):

    # get eventID for csv file name
    eventID = context.event_id

    # Get dictionary object that was entered into firestore
    fields_requested = data["value"]["fields"]

    userEmail = data["value"]["fields"]["currentUserEmail"]["stringValue"]

    # Create emty dataframe
    df = pandas.DataFrame()

    # Create variable for number of rows in the dataframe ...FIGURE THIS OUT!
    number_of_rows = 100

    create_fields(fields_requested, df, number_of_rows)

    # Use /tmp for writable file!
    # https://cloud.google.com/functions/docs/concepts/exec#file_system
    df.to_csv(f'/tmp/{eventID}.csv', index=False)

    del df

    print(context)
    print(data)

    send_email('pupa.matt@gmail.com'
                , userEmail
                , 'test email'
                , 'Here is your data'
                , f'/tmp/{eventID}.csv'
                )




    # https://sendgrid.com/

# https://docs.python.org/3/library/io.html
# https://cmdlinetips.com/2020/05/how-to-save-pandas-dataframe-as-gzip-zip-file/
