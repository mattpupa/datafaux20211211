
from google.cloud import bigquery
from google.oauth2 import service_account

# https://googleapis.dev/python/google-api-core/latest/auth.html
credentials = service_account.Credentials.from_service_account_file(
    'bigquerykey.json', scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

# User Info
list_company = []
list_name = []
list_id = []
list_username = []
list_job = []
# Contact Info
list_address = []
list_email = []
list_phone = []
list_url = []
# Credit Card Info
list_credit_card_full = []
list_credit_card_provider = []
list_credit_card_number = []
list_credit_card_expire = []
list_credit_card_security_code = []
# Bank Info
list_bank_country = []
list_bban = []
list_iban = []
# Currency Info
list_currency_name = []
list_currency_code = []
list_cryptocurrency_name = []
list_cryptocurrency_code = []
# Date Info
list_am_pm = []
list_date = []
list_day_of_month = []
list_day_of_week = []
list_month = []
list_month_name = []
list_year = []
# Color Info
list_color_name = []
list_web_safe_color_name = []
list_hex_color = []
list_rgb_color = []
list_rgb_css_color = []
# Misc Info
list_barcode_ean8 = []
list_barcode_ean13 = []
list_image_url = []
list_latitude = []
list_longitude = []
list_license_plate = []


##################### User Functions #####################
def populate_company(row_count):
    query_company =  f"""
        SELECT distinct company
        FROM `datafaux-ab0de.datafaux_100K.faker_company`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_company = client.query(query_company) # Make the API request
    for row in query_job_company:
        list_company.append(row['company'])

    del query_job_company

    return list_company


def populate_name(row_count):
    query_name =  f"""
        SELECT distinct name
        FROM `datafaux-ab0de.datafaux_100K.faker_name`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_name = client.query(query_name) # Make the API request
    for row in query_job_name:
        list_name.append(row['name'])

    del query_job_name

    return list_name


def populate_id(row_count):
    query_id =  f"""
        SELECT distinct id
        FROM `datafaux-ab0de.datafaux_100K.faker_id`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_id = client.query(query_id) # Make the API request
    for row in query_job_id:
        list_id.append(row['id'])

    del query_job_id

    return list_id


def populate_username(row_count):
    query_username =  f"""
        SELECT distinct username
        FROM `datafaux-ab0de.datafaux_100K.faker_username`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_username = client.query(query_username) # Make the API request
    for row in query_job_username:
        list_username.append(row['username'])

    del query_job_username

    return list_username

def populate_job(row_count):
    query_job =  f"""
        SELECT job_title
        FROM `datafaux-ab0de.datafaux_100K.faker_job`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_job = client.query(query_job) # Make the API request
    for row in query_job_job:
        list_job.append(row['job_title'])

    del query_job_job

    return list_job

##################### Contact Functions #####################
def populate_address(row_count):
    query_address =  f"""
        SELECT distinct address
        FROM `datafaux-ab0de.datafaux_100K.faker_address`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_address = client.query(query_address) # Make the API request
    for row in query_job_address:
        list_address.append(row['address'])

    del query_job_address

    return list_address


def populate_email(row_count):
    query_email =  f"""
        SELECT distinct email
        FROM `datafaux-ab0de.datafaux_100K.faker_email`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_email = client.query(query_email) # Make the API request
    for row in query_job_email:
        list_email.append(row['email'])

    del query_job_email

    return list_email


def populate_phone(row_count):
    query_phone =  f"""
        SELECT distinct phone_number
        FROM `datafaux-ab0de.datafaux_100K.faker_phone`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_phone = client.query(query_phone) # Make the API request
    for row in query_job_phone:
        list_phone.append(row['phone_number'])

    del query_job_phone

    return list_phone


def populate_url(row_count):
    query_url =  f"""
        SELECT distinct website_url
        FROM `datafaux-ab0de.datafaux_100K.faker_website`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_url = client.query(query_url) # Make the API request
    for row in query_job_url:
        list_url.append(row['website_url'])

    del query_job_url

    return list_url


##################### Credit Card Functions #####################
def populate_credit_card_full(row_count):
    query_credit_card_full =  f"""
        SELECT credit_card_full
        FROM `datafaux-ab0de.datafaux_100K.faker_credit_card_full`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_credit_card_full = client.query(query_credit_card_full) # Make the API request
    for row in query_job_credit_card_full:
        list_credit_card_full.append(row['credit_card_full'])

    del query_job_credit_card_full

    return list_credit_card_full


def populate_credit_card_provider(row_count):
    query_credit_card_provider =  f"""
        SELECT credit_card_provider
        FROM `datafaux-ab0de.datafaux_100K.faker_credit_card_provider`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_credit_card_provider = client.query(query_credit_card_provider) # Make the API request
    for row in query_job_credit_card_provider:
        list_credit_card_provider.append(row['credit_card_provider'])

    del query_job_credit_card_provider

    return list_credit_card_provider


def populate_credit_card_number(row_count):
    query_credit_card_number =  f"""
        SELECT credit_card_number
        FROM `datafaux-ab0de.datafaux_100K.faker_credit_card_number`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_credit_card_number = client.query(query_credit_card_number) # Make the API request
    for row in query_job_credit_card_number:
        list_credit_card_number.append(row['credit_card_number'])

    del query_job_credit_card_number

    return list_credit_card_number


def populate_credit_card_expire(row_count):
    query_credit_card_expire =  f"""
        SELECT credit_card_expire
        FROM `datafaux-ab0de.datafaux_100K.faker_credit_card_expire`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_credit_card_expire = client.query(query_credit_card_expire) # Make the API request
    for row in query_job_credit_card_expire:
        list_credit_card_expire.append(row['credit_card_expire'])

    del query_job_credit_card_expire

    return list_credit_card_expire


def populate_credit_card_security_code(row_count):
    query_credit_card_security_code =  f"""
        SELECT credit_card_security_code
        FROM `datafaux-ab0de.datafaux_100K.faker_credit_card_security_code`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_credit_card_security_code = client.query(query_credit_card_security_code) # Make the API request
    for row in query_job_credit_card_security_code:
        list_credit_card_security_code.append(row['credit_card_security_code'])

    del query_job_credit_card_security_code

    return list_credit_card_security_code


##################### Bank Functions #####################
def populate_bank_country(row_count):
    query_bank_country =  f"""
        SELECT bank_country
        FROM `datafaux-ab0de.datafaux_100K.faker_bank_country`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_bank_country = client.query(query_bank_country) # Make the API request
    for row in query_job_bank_country:
        list_bank_country.append(row['bank_country'])

    del query_job_bank_country

    return list_bank_country


def populate_basic_bank_account(row_count):
    query_bban =  f"""
        SELECT basic_bank_account
        FROM `datafaux-ab0de.datafaux_100K.faker_bban`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_basic_bank_account = client.query(query_bban) # Make the API request
    for row in query_job_basic_bank_account:
        list_bban.append(row['basic_bank_account'])

    del query_job_basic_bank_account

    return list_bban


def populate_international_bank_account(row_count):
    query_iban =  f"""
        SELECT international_bank_account
        FROM `datafaux-ab0de.datafaux_100K.faker_iban`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_international_bank_account = client.query(query_iban) # Make the API request
    for row in query_job_international_bank_account:
        list_iban.append(row['international_bank_account'])

    del query_job_international_bank_account

    return list_iban


##################### Currency Functions #####################
def populate_currency_name(row_count):
    query_currency_name =  f"""
        SELECT currency_name
        FROM `datafaux-ab0de.datafaux_100K.faker_currency_name`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_currency_name = client.query(query_currency_name) # Make the API request
    for row in query_job_currency_name:
        list_currency_name.append(row['currency_name'])

    del query_job_currency_name

    return list_currency_name


def populate_currency_code(row_count):
    query_currency_code =  f"""
        SELECT currency_code
        FROM `datafaux-ab0de.datafaux_100K.faker_currency_code`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_currency_code = client.query(query_currency_code) # Make the API request
    for row in query_job_currency_code:
        list_currency_code.append(row['currency_code'])

    del query_job_currency_code

    return list_currency_code


def populate_cryptocurrency_name(row_count):
    query_cryptocurrency_name =  f"""
        SELECT cryptocurrency_name
        FROM `datafaux-ab0de.datafaux_100K.faker_cryptocurrency_name`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_cryptocurrency_name = client.query(query_cryptocurrency_name) # Make the API request
    for row in query_job_cryptocurrency_name:
        list_cryptocurrency_name.append(row['cryptocurrency_name'])

    del query_job_cryptocurrency_name

    return list_cryptocurrency_name


def populate_cryptocurrency_code(row_count):
    query_cryptocurrency_code =  f"""
        SELECT cryptocurrency_code
        FROM `datafaux-ab0de.datafaux_100K.faker_cryptocurrency_code`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_cryptocurrency_code = client.query(query_cryptocurrency_code) # Make the API request
    for row in query_job_cryptocurrency_code:
        list_cryptocurrency_code.append(row['cryptocurrency_code'])

    del query_job_cryptocurrency_code

    return list_cryptocurrency_code


##################### Date Functions #####################
def populate_am_pm(row_count):
    query_am_pm =  f"""
        SELECT am_pm_flag
        FROM `datafaux-ab0de.datafaux_100K.faker_am_pm`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_am_pm = client.query(query_am_pm) # Make the API request
    for row in query_job_am_pm:
        list_am_pm.append(row['am_pm_flag'])

    del query_job_am_pm

    return list_am_pm


def populate_date(row_count):
    query_date =  f"""
        SELECT date
        FROM `datafaux-ab0de.datafaux_100K.faker_date`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_date = client.query(query_date) # Make the API request
    for row in query_job_date:
        list_date.append(row['date'])

    del query_job_date

    return list_date


def populate_day_of_month(row_count):
    query_day_of_month =  f"""
        SELECT day_of_month
        FROM `datafaux-ab0de.datafaux_100K.faker_day_of_month`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_day_of_month = client.query(query_day_of_month) # Make the API request
    for row in query_job_day_of_month:
        list_day_of_month.append(row['day_of_month'])

    del query_job_day_of_month

    return list_day_of_month


def populate_day_of_week(row_count):
    query_day_of_week =  f"""
        SELECT day_of_week
        FROM `datafaux-ab0de.datafaux_100K.faker_day_of_week`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_day_of_week = client.query(query_day_of_week) # Make the API request
    for row in query_job_day_of_week:
        list_day_of_week.append(row['day_of_week'])

    del query_job_day_of_week

    return list_day_of_week


def populate_month(row_count):
    query_month =  f"""
        SELECT month
        FROM `datafaux-ab0de.datafaux_100K.faker_month`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_month = client.query(query_month) # Make the API request
    for row in query_job_month:
        list_month.append(row['month'])

    del query_job_month

    return list_month


def populate_month_name(row_count):
    query_month_name =  f"""
        SELECT month_name
        FROM `datafaux-ab0de.datafaux_100K.faker_month_name`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_month_name = client.query(query_month_name) # Make the API request
    for row in query_job_month_name:
        list_month_name.append(row['month_name'])

    del query_job_month_name

    return list_month_name


def populate_year(row_count):
    query_year =  f"""
        SELECT year
        FROM `datafaux-ab0de.datafaux_100K.faker_year`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_year = client.query(query_year) # Make the API request
    for row in query_job_year:
        list_year.append(row['year'])

    del query_job_year

    return list_year


##################### Color Functions #####################
def populate_color_name(row_count):
    query_color_name =  f"""
        SELECT color_name
        FROM `datafaux-ab0de.datafaux_100K.faker_color`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_color_name = client.query(query_color_name) # Make the API request
    for row in query_job_color_name:
        list_color_name.append(row['color_name'])

    del query_job_color_name

    return list_color_name


def populate_web_safe_color_name(row_count):
    query_web_safe_color_name =  f"""
        SELECT safe_color_name
        FROM `datafaux-ab0de.datafaux_100K.faker_safe_color`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_web_safe_color_name = client.query(query_web_safe_color_name) # Make the API request
    for row in query_job_web_safe_color_name:
        list_web_safe_color_name.append(row['safe_color_name'])

    del query_job_web_safe_color_name

    return list_web_safe_color_name


def populate_hex_color(row_count):
    query_hex_color =  f"""
        SELECT hex_color
        FROM `datafaux-ab0de.datafaux_100K.faker_hex_color`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_hex_color = client.query(query_hex_color) # Make the API request
    for row in query_job_hex_color:
        list_hex_color.append(row['hex_color'])

    del query_job_hex_color

    return list_hex_color


def populate_rgb_color(row_count):
    query_rgb_color =  f"""
        SELECT rgb_color
        FROM `datafaux-ab0de.datafaux_100K.faker_rgb_color`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_rgb_color = client.query(query_rgb_color) # Make the API request
    for row in query_job_rgb_color:
        list_rgb_color.append(row['rgb_color'])

    del query_job_rgb_color

    return list_rgb_color


def populate_rgb_css_color(row_count):
    query_rgb_css_color =  f"""
        SELECT rgb_css_color
        FROM `datafaux-ab0de.datafaux_100K.faker_rgb_css_color`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_rgb_css_color = client.query(query_rgb_css_color) # Make the API request
    for row in query_job_rgb_css_color:
        list_rgb_css_color.append(row['rgb_css_color'])

    del query_job_rgb_css_color

    return list_rgb_css_color


##################### Miscellaneous Functions #####################
def populate_barcode_ean8(row_count):
    query_barcode_ean8 =  f"""
        SELECT barcode_ean8
        FROM `datafaux-ab0de.datafaux_100K.faker_barcode_ean8`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_barcode_ean8 = client.query(query_barcode_ean8) # Make the API request
    for row in query_job_barcode_ean8:
        list_barcode_ean8.append(row['barcode_ean8'])

    del query_job_barcode_ean8

    return list_barcode_ean8


def populate_barcode_ean13(row_count):
    query_barcode_ean13 =  f"""
        SELECT barcode_ean13
        FROM `datafaux-ab0de.datafaux_100K.faker_barcode_ean13`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_barcode_ean13 = client.query(query_barcode_ean13) # Make the API request
    for row in query_job_barcode_ean13:
        list_barcode_ean13.append(row['barcode_ean13'])

    del query_job_barcode_ean13

    return list_barcode_ean13


def populate_image_url(row_count):
    query_image_url =  f"""
        SELECT image_url
        FROM `datafaux-ab0de.datafaux_100K.faker_image_url`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_image_url = client.query(query_image_url) # Make the API request
    for row in query_job_image_url:
        list_image_url.append(row['image_url'])

    del query_job_image_url

    return list_image_url


def populate_latitude(row_count):
    query_latitude =  f"""
        SELECT latitude_coordinate
        FROM `datafaux-ab0de.datafaux_100K.faker_latitude`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_latitude = client.query(query_latitude) # Make the API request
    for row in query_job_latitude:
        list_latitude.append(row['latitude_coordinate'])

    del query_job_latitude

    return list_latitude


def populate_longitude(row_count):
    query_longitude =  f"""
        SELECT longitude_coordinate
        FROM `datafaux-ab0de.datafaux_100K.faker_longitude`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_longitude = client.query(query_longitude) # Make the API request
    for row in query_job_longitude:
        list_longitude.append(row['longitude_coordinate'])

    del query_job_longitude

    return list_longitude


def populate_license_plate(row_count):
    query_license_plate =  f"""
        SELECT license_plate
        FROM `datafaux-ab0de.datafaux_100K.faker_license_plate`
        ORDER BY rand()
        LIMIT {row_count}
    """
    query_job_license_plate = client.query(query_license_plate) # Make the API request
    for row in query_job_license_plate:
        list_license_plate.append(row['license_plate'])

    del query_job_license_plate

    return list_license_plate
