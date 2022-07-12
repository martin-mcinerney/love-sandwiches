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
SHEET = GSPREAD_CLIENT.open('Love Sandwiches')

def get_sales_data():
    """
    Get sales input from user
    """
    print("Please enter sales data from last market.")
    print("Data should be 6 numbers seperated by commas.")
    print("Example: 10,23,45,67,43,23\n")
    data_str = input('Enter your data here: ')
    sales_data= data_str.split(',')
    print(sales_data)
    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, turns all strings into integers and raises an error if this cannot be completed or there aren't exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required. You provided {len(values)}"
            )
    except ValueError as e: 
        print(f'Invalid data: {e}, please try again.\n')

get_sales_data()