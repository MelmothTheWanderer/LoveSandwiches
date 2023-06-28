# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')

SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():


    '''Get sales figures from the user'''

    while True:
        print('Please enter sales data from the last market')
        print('Data should be six numbers , seperated by a comma')
        print('Example: 1, 2 , 3, 4 ,5 ,6')

        data_string =    input('Please input your data here: ')
        print(f'The data you submitted was {data_string}')

        sales_data = data_string.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data


def validate_data(values):

    """
    This function convert the string values into integers, and if
    can't be done , then it will return an error , and also , will check to 
    see if the data is 6 digits
    """
    try:

        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError (f"Exactly 6 figures required here , and you have provided {len(values)}")
        
    except ValueError as e: 
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_sales_worksheet(data):

    """Updates the google spreadsheet with new data"""

    print("This is updating the spread sheet with new data./n")

    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfuly/n")

data = get_sales_data()

sales_data = [int{num} for num in data]






