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

get_sales_data()