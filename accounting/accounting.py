# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)
# [id, month, day, year, type, amount]


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
                    'Update existing income/outcome',
                    'Find most profitable year',
                    'Find average profit for given year']
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
        elif menu == '5':
            show_most_profitable_year(table)
        elif menu == '6':
            show_average_profit_for_user_passed_year(table)
        else:
            ui.print_error_message('Choose number from menu')

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
        save_data_to_file(table)
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
    if len(table) > 0:

        show_table(table)
        id_ = ui.get_inputs([''], 'Type id of record to be removed')[0]
        ids = [record[0] for record in table]
        if id_ in ids:
            table = remove(table, id_)
        else:
            ui.print_error_message('Invalid id input')
    
    else:
        ui.print_error_message('There is no data in archive')

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
        save_data_to_file(table)
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
    if len(table) > 0:

        show_table(table)
        id_ = ui.get_inputs([''], 'Type id of record to be changed')[0]
        ids = [record[0] for record in table]
        if id_ in ids:
            table = update(table, id_)
        else:
            ui.print_error_message('Invalid id input')
    else:
        ui.print_error_message("There is no data in archive")

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
        save_data_to_file(table)
    else:
        ui.print_error_message('Invalid input format')
    return table


# special functions:
# ------------------
def get_profit_for_each_year(table):
    """
    Searches table for different years and calculates profit,
    and amount of transactions for each year independetly

    Parameters:
        table - list of lists

    Returns:
        profit - [[year, profit, item_count], [year2, profit2, item_count]...]
    """
    profit = []
    for record in table:
        # if year is not in profit yet
        if record[-3] not in [year[0] for year in profit]:
            # add new formated element to profit list
            profit.append([record[-3], 0, 0])
        if record[-2] == 'in':
            for year in profit:
                if year[0] == record[-3]:
                    year[1] += int(record[-1])
                    year[2] += 1
        if record[-2] == 'out':
            for year in profit:
                if year[0] == record[-3]:
                    year[1] -= int(record[-1])
                    year[2] += 1

    return profit


# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    """
    Searches each year profits for year with highest income

    Parameters:
        table - list of lists
    
    Returns
        int - representing year
    """
    # [id, month, day, year, type, amount]
    profit = get_profit_for_each_year(table)
    year_max = profit[0]
    for year_data in profit:
        if year_data[1] > year_max[1]:
            year_max = year_data

    return int(year_max[0])


def show_most_profitable_year(table):
    """
    Calculates, and displays most profitable year

    Parameters:
        table - list of lists to be searched

    Returns:
        None
    """
    if len(table) > 0:

        max_year = which_year_max(table)
        ui.print_result(str(max_year), 'Most profitable year')
    
    else:
        ui.print_error_message('There is no data in archive')


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    """
    Calculates average income for choosen year

    Parameters:
        table - list of lists
        year -  int for which average should be returned
    
    Returns:
        average - int
    """
    profit = get_profit_for_each_year(table)
    average = None
    for year_data in profit:
        if int(year_data[0]) == year:
            average = year_data[1]/year_data[2]
    return average


def show_average_profit_for_user_passed_year(table):
    """
    Calculates, and displays most profitable year provided
    from user

    Parameters:
        table - list of lists to be searched

    Returns:
        None
    """
    if len(table) > 0:

        year = ui.get_inputs([''], 'Choose year to calculate')[0]
        if common.is_year_valid(year):
            average = avg_amount(table, int(year))
            if average != None:
                average = str(round(average, 2))
                ui.print_result(average, 'The average profit for {} year was'.format(year))
            else:
                ui.print_error_message('There is no data for {} year.'.format(year))
        else:
            ui.print_error_message('Invalid input')

    else:
        ui.print_error_message('There is no data in archive')