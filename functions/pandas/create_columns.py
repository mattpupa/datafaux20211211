
from populate_functions import populate_name, populate_address, populate_id, populate_company, populate_date, populate_username, populate_email


# CAN THIS BE OPTIMIZED ?!?!?
# https://stackoverflow.com/questions/4246000/how-to-call-python-functions-dynamically
def create_fields(request_columns, dataframe, number_of_rows):
    for col in request_columns:
        if col == 'name' and request_columns[col]['stringValue'] == 'true':
            populate_name(dataframe, number_of_rows)
        elif col == 'address' and request_columns[col]['stringValue'] == 'true':
            populate_address(dataframe, number_of_rows)
        elif col == 'id' and request_columns[col]['stringValue'] == 'true':
            populate_id(dataframe, number_of_rows)
        elif col == 'company' and request_columns[col]['stringValue'] == 'true':
            populate_company(dataframe, number_of_rows)
        elif col == 'date' and request_columns[col]['stringValue'] == 'true':
            populate_date(dataframe, number_of_rows)
        elif col == 'userName' and request_columns[col]['stringValue'] == 'true':
            populate_username(dataframe, number_of_rows)
        elif col == 'email' and request_columns[col]['stringValue'] == 'true':
            populate_email(dataframe, number_of_rows)
        else:
            pass
