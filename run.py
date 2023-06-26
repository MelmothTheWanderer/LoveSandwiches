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
    
    print('Please enter sales data from the last market')
    print('Data should be six numbers , seperated by a comma')
    print('Example: 1, 2 , 3, 4 ,5 ,6')

    data_string =    input('Please input your data here: ')
    print(f'The data you submitted was {data_string}')

    sales_data = data_string.split(",")
    validate_data(sales_data)


def validate_data(values):
    """
    This function convert the string values into integers, and if
    can't be done , then it will return an error , and also , will check to 
    see if the data is 6 digits
    """
    # print(values)
    # use a try to see if there is 6 numbers
    try:
        if len(values) != 6:
            raise ValueError (f"Exactly 6 figures required here , and you have provided {len(values)}")
        
    except ValueError as e : 
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()






