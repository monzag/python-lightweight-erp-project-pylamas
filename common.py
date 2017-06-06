# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''

    # your code

    return generated


def is_year_valid(year):
    """
    determines if user input is a valid format for year

    Paramteters
        year - string from user

    Returns:
        boolean
    """
    if year.isdigit() and len(year) == 4:
        if int(year) > 1950 and int(year) < 2018:
            return True
    return False


def is_day_valid(day):
    """
    determines if user input is a valid format for day

    Paramteters
        day - string from user

    Returns:
        boolean
    """
    if day.isdigit() and len(day) == 2:
        if int(day) > 0 and int(day) < 32 and len(day) == 2:
            return True
    return False


def is_month_valid(month):
    """
    determines if user input is a valid format for day

    Paramteters
        month - string from user

    Returns:
        boolean
    """
    if month.isdigit() and len(month) == 2:
        if int(month) > 0 and int(month) < 13:
            return True
    return False


def is_money_valid(money):
    """
    determines if user input is a valid format for money

    Paramteters
        money - string from user

    Returns:
        boolean
    """
    # to implement floats -> e.x. 129.45
    if money.isdigit() and money[0] != '0':
        return True
    return False
