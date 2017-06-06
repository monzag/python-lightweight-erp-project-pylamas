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
    # zmniejszę to, obiecuję :D
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    special_char = ['#', '$', '%', '&', '!']
    letter_low = [
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z'
                 ]

    letter_upper = [item.upper() for item in letter_low]
    digit = random.randrange(10)

    generated = ''
    count = 0
    while count < 8:
        if count < 5:
            generated += random.choice(letter_low)
            generated += random.choice(letter_upper)
            generated += str(digit)
            count += 3

        elif count > 5:
            generated += random.choice(special_char)
            count += 1

        for item in table:
            if item == generated:
                count = 0

    return generated


def find_id(table, id_):
    '''In list of lists find record by id number. Return record.
    Use in remove() and update()'''

    for record in table:
        for item in record:
            if item == id_:
                return record


def remove_record(table, record):
    '''Remove record (list of lists) in table. Return table. Use in remove()'''

    for index, item in enumerate(table):
        if item == record:
            table.pop(index)

    return table


def insert_new_data(record, new_data, position):
    '''Replace old data with new_data on proper position in record (list of lists). 
    Return record. Use in update()'''

    record[position] = new_data
    return record


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

