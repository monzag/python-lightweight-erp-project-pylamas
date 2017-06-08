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
                generated = ''

    return generated


def find_id(table, id_):
    '''
    Find record by id number.

    Args:
        table - list in lists when element with index 0 is id number
        id_ - unique string for user

    Returns:
         record - list from table
    '''

    for record in table:
        if record[0] == id_:
            return record


def remove_record(table, record):
    '''Find specific record and its index. Remove it from table.

    Args:
        table - list in lists
        record - list from table

    Returns:
        table without specified record
    '''

    for index, item in enumerate(table):
        if item == record:
            table.pop(index)

    return table


def insert_new_data(record, new_data, option):
    '''
    Replace old data with new_data on proper position in record.

    Args:
        record - list from table with proper id
        new_data - new string insert in old place
        option - int, index in record

    Returns:
         record with new data
    '''

    record[option] = new_data
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
    if day.isdigit():
        if int(day) > 0 and int(day) < 32:
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
    if month.isdigit():
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


def get_value_from(table, index):
    '''creates list of values from exact index

    Parameters:
        table - list of lists
        index - int corresponding to value in table

    Returns:
        values - list of value
    '''

    values = [record[index] for record in table]

    return values


