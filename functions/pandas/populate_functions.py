
import faker


# Create function to fill dataframe with fake name
def populate_name(dataframe, row_count):
    global name_list
    name_list = []
    for i in range(row_count):
        name_list.append(faker.Faker().name())
    dataframe['Name'] = name_list


# Create function to fill dataframe with fake address
def populate_address(dataframe, row_count):
    global address_list
    address_list = []
    for i in range(row_count):
        address_list.append(faker.Faker().address())
    dataframe['Address'] = address_list

# Create function to fill dataframe with fake IDs
def populate_id(dataframe, row_count):
    global id_list
    id_list = []
    for i in range(row_count):
        id_list.append(faker.Faker().bban())
    dataframe['ID'] = id_list

# Create function to fill dataframe with fake company
def populate_company(dataframe, row_count):
    global company_list
    company_list = []
    for i in range(row_count):
        company_list.append(faker.Faker().company())
    dataframe['Company'] = company_list

# Create function to fill dataframe with fake dates
def populate_date(dataframe, row_count):
    global date_list
    date_list = []
    for i in range(row_count):
        date_list.append(faker.Faker().date())
    dataframe['Date'] = date_list

# Create function to fill dataframe with fake user names
def populate_username(dataframe, row_count):
    global username_list
    username_list = []
    for i in range(row_count):
        username_list.append(faker.Faker().user_name())
    dataframe['Username'] = username_list

# Create function to fill dataframe with fake emails
def populate_email(dataframe, row_count):
    global email_list
    email_list = []
    for i in range(row_count):
        email_list.append(faker.Faker().email())
    dataframe['Email'] = email_list
