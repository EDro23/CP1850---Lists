"""
This module contains functions for getting 
sales data from a user.
"""


def get_amount() -> float:
    """
    

    Returns
    -------
    amount
        Gets a sales amount from the user,
        converts it to a float value, and returns the int value.

    """
    program = True
    while program:
        amount = float(input("Amount:\t\t\t"))
        if amount > 0:
            return amount
        else:
            print("Sales amount must be greater than 0.")
          


def get_day(month) -> int:
    """
    

    Returns
    -------
    day 
        Gets a day from the user, converts it to an int value, and returns the int value.

    """
    if month == 2:
        max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31
    program = True
    while program:
        day = int(input(f"Day (1-{max_days}):\t\t"))
        
        if day > 31 or day < 0:
            print("The sales day needs to be within your specific month.")
        else:
            program = False
            return day

def get_month() -> int:
    """
    

    Returns
    -------
    month 
        Gets a month from the user, converts it to an int value, and returns the int value.

    """
    program = True
    while program:
        month = int(input("Month (1-12):\t"))
        if month >= 1 and month <= 12:
            return month
        else:
            print("Month should be between 1 and 12")
        

def get_year() -> int:
    """
    

    Returns
    -------
    year
        Gets the year from the user, converts it to an int value, and returns the int value.

    """
    program = True
    while program:
        
        year = int(input("Year:\t\t\t"))
        if year < 1900 or year > 3000:
            print("You must enter a year between 1900 to 3000.")
        else:
            program = False
            return year