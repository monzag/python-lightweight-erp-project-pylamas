# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    table = get_data_from_file()
    table = menu_control(table)
    save_data_to_file(table)


def get_data_from_file():
    """
    Create data for accounting based on csv file if exists
    if not returns empty list

    Returns:
        table - list of lists corresponding to data model
    """
    file_path = os.getcwd() + '/accounting/items.csv'
    if os.path.exists(file_path):
        table = data_manager.get_table_from_file(file_path)
    else:
        table = []
    return table


def save_data_to_file(table):
    """
    Exports data to file using data_menager module

    Parameters:
        table - list of list
    Returns:
        None
    """
    file_path = os.getcwd() + '/accounting/items.csv'
    data_manager.write_table_to_file(file_path, table)


def menu_control(table):
    """
    Main loop of module sales
    Controls operations on table depending on user choices

    Parameters:
        table - list of lists containing data
        
    Returns:
        table - list of lists
    """
    TITLE = 'Accounting archive'
    LIST_OPTIONS = ['Show archived incomes/outcomes',
                    'Add to archive  income/outcome',
                    'Remove existing income/outcome',
                    'Update existing income/outcome']
    EXIT_MESSAGE = 'Back to main menu'

    menu = None
    while menu != '0':
        ui.print_menu(TITLE, LIST_OPTIONS, EXIT_MESSAGE)
        menu = ui.get_inputs([''], 'Choose action to perform')[0]
        
        if menu == '1':
            show_table(table)
        elif menu == '2':
            table = add(table)
        elif menu == '3':
            table = remove_record_from_data(table)
        elif menu == '4':
            table = update_record_in_data(table)

    return table


def show_table(table):
    """
    Display a table defined in module ui

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    TITLE_LIST = ['id', 'month', 'day', 'year', 'type', 'amount']
    ui.print_table(table, TITLE_LIST)
 

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    new_record = get_record_from_user()

    if is_record_valid(new_record):
        id_ = common.generate_random(table)
        new_record.insert(0, id_)
        table.append(new_record)
    else:
        ui.print_error_message('Invalid input format.\nYour record will not be added to archive.')

    return table


def get_record_from_user():
    """
    Creates record based on user input

    Returns:
        new_record - list with 5 elements
    """
    LIST_LABLES = ['month(mm)', 'day(dd)', 'year(yyyy)', 'type(in/out)', 'amount($)']
    new_record = ui.get_inputs(LIST_LABLES, 'Archive new accounting')
    return new_record


def is_record_valid(record):
    """
    Seperates user input into categories and determines
    whenever were provided corectlly

    Rerurns:
        booolean
    """
    [month, day, year, in_out, amount] = record
    return is_date_valid(month, day, year) and is_value_valid(in_out, amount)


def is_date_valid(month, day, year):
    """
    Determines if user input date was of good format

    Parameters:
        day: str
        month: str
        year: str

    Returns:
        True : if date format was corect
        False : otherwise
    """
    return common.is_month_valid(month) and common.is_day_valid(day) and common.is_year_valid(year)


def is_value_valid(in_out, amount):
    """
    Determines whenever user input was correct

    Parameters:
        in_out: str
        amount: str

    Returns:
        True: if user input was correct
        False: otherwise
    """
    return in_out in ['in', 'out'] and common.is_money_valid(amount)


def remove_record_from_data(table):
    """
    Removes specified by user record from data if possible

    Parameters
        table : list of lists to remove list from

    Returns:
        table : list of lists (updated)
    """
    show_table(table)
    id_ = ui.get_inputs([''], 'Type id of record to be removed')[0]
    ids = [record[0] for record in table]
    if id_ in ids:
        table = remove(table, id_)
    else:
        ui.print_error_message('Invalid id input')
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """
    for index, record in enumerate(table):
        if record[0] == id_: # where record[0] is id
            table.pop(index)
    return table


def update_record_in_data(table):
    """
    Specifies record which user would like to change,
    and determines if it's possible

    Parameters:
        table - list of lists containing data

    Returns:
        table - list of lists (updated)
    """
    show_table(table)
    id_ = ui.get_inputs([''], 'Type id of record to be changed')[0]
    ids = [record[0] for record in table]
    if id_ in ids:
        table = update(table, id_)
    else:
        ui.print_error_message('Invalid id input')
    return table


def update(table, id_):
    """
    Updates record with exact >id< in the table. Ask users for new data.
    If new data is correct, changes record.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """
    updated_record = get_record_from_user()
    if is_record_valid(updated_record):
        for index, record in enumerate(table):
            if record[0] == id_:
                table[index] = record[:1] + updated_record
    else:
        ui.print_error_message('Invalid input format')
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
