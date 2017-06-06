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
    file_path = os.getcwd() + '/accounting/items.csv'
    table = get_archive(file_path)

    title = 'Accounting archive'
    list_options = ['Show archived incomes/outcomes',
                    'Add to archive  income/outcome',
                    'Remove existing income/outcome',
                    'Update existing income/outcome']
    exit_message = 'Back to main menu'
    
    menu = None
    while menu != '0':
        ui.print_menu(title, list_options, exit_message)
        menu = ui.get_inputs([''], 'Choose action to perform')[0]
        
        if menu == '1':
            show_table(table)
        if menu == '2':
            add(table)
        if menu == '3':
            remove(table, id_)
        if menu == '4':
            update(table, id_)
        if menu == '0':
            data_manager.write_table_to_file(file_path, table)
        else:
            ui.print_error_message('Invalid input')


def get_archive(file_path):
    if os.path.exists(file_path):
        table = data_manager.get_table_from_file(file_path)
    else:
        table = []
    return table


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
    ui.print_table(table, title_list)
 

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    list_lables = ['month(mm)', 'day(dd)', 'year(yyyy)', 'type(in/out)', 'amount($)']
    new_record = ui.get_inputs(list_lables, 'Archive new accounting')

    if is_record_valid(new_record):
        ids = [each[0] for each in table]
        id_ = common.generate_random(ids)
        new_record.insert(0, id_)
        table.append(new_record)
    else:
        ui.print_error_message('Invalid input format.\nYour record will not be added to archive.')

    return table


def is_record_valid(record):
    """
    unpacks provided list into ordered values and checks if input from user was proper

    Parameters:
        record - list of values
    
    Returns:if len(str(title_list[item_index])) > len(longest_string):
        boolean
    """
    [month, day, year, in_out, amount] = record
    return is_date_valid(month, day, year) and is_value_vaild(in_out, amount)


def is_date_valid(month, day, year):
    return common.is_month_valid(month) and common.is_day_valid(day) and common.is_year_valid(year)


def is_value_vaild(in_out, amount):
    return in_out in ['in', 'out'] and common.is_money_valid(amount)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

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
