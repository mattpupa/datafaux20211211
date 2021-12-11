
from populate_functions import populate_company, populate_name, populate_id, populate_username, populate_job
from populate_functions import populate_address, populate_email, populate_phone, populate_url
from populate_functions import populate_credit_card_full, populate_credit_card_provider, populate_credit_card_number, populate_credit_card_expire, populate_credit_card_security_code
from populate_functions import populate_bank_country, populate_basic_bank_account, populate_international_bank_account
from populate_functions import populate_currency_name, populate_currency_code, populate_cryptocurrency_name, populate_cryptocurrency_code
from populate_functions import populate_am_pm, populate_date, populate_day_of_month, populate_day_of_week, populate_month, populate_month_name, populate_year
from populate_functions import populate_color_name, populate_web_safe_color_name, populate_hex_color, populate_rgb_color, populate_rgb_css_color
from populate_functions import populate_barcode_ean8, populate_barcode_ean13, populate_image_url, populate_latitude, populate_longitude, populate_license_plate

records = []
columns = []

# CAN THIS BE OPTIMIZED ?!?!?
# https://stackoverflow.com/questions/4246000/how-to-call-python-functions-dynamically
def create_fields(request_columns, number_of_rows):
    for col in request_columns:
        # User info
        if col == 'company' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_company(number_of_rows))
        elif col == 'name' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_name(number_of_rows))
        elif col == 'id' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_id(number_of_rows))
        elif col == 'username' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_username(number_of_rows))
        elif col == 'job' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_job(number_of_rows))
        # Contact info
        elif col == 'address' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_address(number_of_rows))
        elif col == 'email' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_email(number_of_rows))
        elif col == 'phone' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_phone(number_of_rows))
        elif col == 'url' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_url(number_of_rows))
        # Credit Card info
        elif col == 'creditcardfull' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_credit_card_full(number_of_rows))
        elif col == 'creditcardprovider' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_credit_card_provider(number_of_rows))
        elif col == 'creditcardnumber' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_credit_card_number(number_of_rows))
        elif col == 'creditcardexpire' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_credit_card_expire(number_of_rows))
        elif col == 'creditcardsecuritycode' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_credit_card_security_code(number_of_rows))
        # Bank info
        elif col == 'bankcountry' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_bank_country(number_of_rows))
        elif col == 'bban' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_basic_bank_account(number_of_rows))
        elif col == 'iban' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_international_bank_account(number_of_rows))
        # Currency info
        elif col == 'currencyname' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_currency_name(number_of_rows))
        elif col == 'currencycode' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_currency_code(number_of_rows))
        elif col == 'cryptocurrencyname' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_cryptocurrency_name(number_of_rows))
        elif col == 'cryptocurrencycode' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_cryptocurrency_code(number_of_rows))
        # Date info
        elif col == 'ampm' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_am_pm(number_of_rows))
        elif col == 'date' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_date(number_of_rows))
        if col == 'dayofmonth' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_day_of_month(number_of_rows))
        elif col == 'dayofweek' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_day_of_week(number_of_rows))
        elif col == 'month' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_month(number_of_rows))
        elif col == 'monthname' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_month_name(number_of_rows))
        elif col == 'year' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_year(number_of_rows))
        # Color info
        elif col == 'colorname' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_color_name(number_of_rows))
        elif col == 'websafecolorname' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_web_safe_color_name(number_of_rows))
        if col == 'hexcolor' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_hex_color(number_of_rows))
        elif col == 'rgbcolor' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_rgb_color(number_of_rows))
        elif col == 'rgbcsscolor' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_rgb_css_color(number_of_rows))
        # Miscellaneous info
        elif col == 'ean8' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_barcode_ean8(number_of_rows))
        elif col == 'ean13' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_barcode_ean13(number_of_rows))
        if col == 'imageurl' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_image_url(number_of_rows))
        elif col == 'latitude' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_latitude(number_of_rows))
        elif col == 'longitude' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_longitude(number_of_rows))
        elif col == 'licenseplate' and request_columns[col]['stringValue'] == 'true':
            records.append(populate_license_plate(number_of_rows))
        else:
            pass

    return records


def create_columns(request_columns):
    for col in request_columns:
        # User info
        if col == 'company' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'name' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'id' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'username' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'job' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Contact info
        elif col == 'address' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'email' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'phone' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'url' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Credit Card info
        elif col == 'creditcardfull' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'creditcardprovider' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'creditcardnumber' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'creditcardexpire' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'creditcardsecuritycode' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Bank info
        elif col == 'bankcountry' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'bban' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'iban' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Currency info
        elif col == 'currencyname' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'currencycode' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'cryptocurrencyname' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'cryptocurrencycode' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Date info
        elif col == 'ampm' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'date' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        if col == 'dayofmonth' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'dayofweek' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'month' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'monthname' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'year' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Color info
        elif col == 'colorname' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'websafecolorname' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        if col == 'hexcolor' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'rgbcolor' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'rgbcsscolor' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        # Miscellaneous info
        elif col == 'ean8' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'ean13' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        if col == 'imageurl' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'latitude' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'longitude' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        elif col == 'licenseplate' and request_columns[col]['stringValue'] == 'true':
            columns.append(col)
        else:
            pass

    return columns
