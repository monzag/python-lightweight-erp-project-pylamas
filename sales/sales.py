# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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
    file_path = os.getcwd() + '/sales/sales.csv'
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
    file_path = os.getcwd() + '/sales/sales.csv'
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
    TITLE = 'Sales archive'
    LIST_OPTIONS = ['Show archived sales',
                    'Add new sale',
                    'Remove existing sale',
                    'Update existing sale',
                    'Get id of item with lowest price',
                    'Print items between dates']
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
            show_lowest_id(table)
        elif menu == '6':
            show_items_sold_between_user_passed_dates(table)
        else:
            ui.print_error_message('Choose number from menu')

    return table


def show_table(table):
    """
    Display data in formated table defined in ui module

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    TITLE_LIST = ['id', 'title', 'price', 'month', 'day', 'year']
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

    if is_record_vaild(new_record):
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
    LIST_LABLES = ['title', 'price($)', 'month(mm)', 'day(dd)', 'year(yyyy)']
    new_record = ui.get_inputs(LIST_LABLES, 'Archive new sale')

    return new_record


def is_record_vaild(record):
    """
    Seperates user input into categories and determines
    whenever were provided corectlly

    Rerurns:
        booolean
    """
    [title, price, month, day, year] = record
    return common.is_money_valid(price) and is_date_vaild(day, month, year)


def is_date_vaild(day, month, year):
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
    return common.is_day_valid(day) and common.is_month_valid(month) and common.is_year_valid(year)


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
        ui.print_error_message('There is no data in archive')

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

    if is_record_vaild(updated_record):
        for index, record in enumerate(table):
            if record[0] == id_:
                table[index] = record[:1] + updated_record
        save_data_to_file(table)
    else:
        ui.print_error_message('Invalid input format')

    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    """
    Function finds item with lowest price. If items have same price it will
    alphabeticly lower items id

    Parameters:
        table - list of lists to find item in
    
    Returns:
        str : id of a lowest priced item
    """
    lowest_price = table[0]
    for record in table:
        # if price is same
        if int(record[2]) == int(lowest_price[2]): # were ...[2] is a price
            # compere ASCII values of strings
            if record[1].upper() < lowest_price[1].upper():
                lowest_price = record
        elif int(record[2]) < int(lowest_price[2]):
            lowest_price = record

    return lowest_price[0] # which is id


def show_lowest_id(table):
    """
    Finds and prints id of an item with a lowest price
    
    Parameters:
        table - list of lists to search in
    
    Returns:
        None
    """
    if len(table) > 0:

        lowest_id = get_lowest_price_item_id(table)
        ui.print_result(lowest_id, 'Id of a lowest priced item')

    else:
        ui.print_error_message('There is no data in archive.')

# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Searches table for records which dates are between given borders,
    using string ASCII comprehensions

    Parameters:
        strs : year_from, month_from, day_from
        strs : year_to, month_to, day_to
    
    Returns:
        items_between - list of lists (records that pass comprehension)
    """
    # record = [id, title, price, (-3)month, (-2)day, (-1)year]
    from_date = format_date([year_from, month_from, day_from])
    to_date = format_date([year_to, month_to, day_to])
    items_between = []
    for record in table:
        sale_date = [record[-1], record[-3], record[-2]]
        sale_date = format_date(sale_date)
        if from_date < sale_date and sale_date < to_date:
            record = record[:2] + [int(element) for element in record[2:]]
            items_between.append(record)

    return items_between


def format_date(date_list):
    """
    formats given date as string 'yyyy:mm:dd'

    Parameters:
        date_list - list of ints [yyyy, mm, dd]
    
    Returns:
        str : 'yyyy:mm:dd'
    """
    for i, element in enumerate(date_list):
        if len(str(element)) == 1:
            date_list[i] = '0' + str(element)
        else:
            date_list[i] = str(element)

    return ':'.join(date_list)


def show_items_sold_between_user_passed_dates(table):
    """
    Holds step by step behaviour of func >get_lowest_price_item_id< in menu
        1) get dates from user
        2) check if is valid
        3) call get_lowest_price_item_id
        4) show result
    
    Parameters:
        table - list of lists to search in
    
    Returns:
        None
    """
    DATE_LABELS = ['year from', 'month from', 'day from', 'year to', 'month to', 'day_to']
    date = ui.get_inputs(DATE_LABELS, 'Input dates')

    [year_from, month_from, day_from, year_to, month_to, day_to] = date

    if is_date_vaild(day_from, month_from, year_from) and is_date_vaild(day_to, month_to, year_to):
        items_between = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        
        for index, record in enumerate(items_between):
            items_between[index] = record[:2] + [str(element) for element in record[2:]]

        show_table(items_between)

    else:
        ui.print_error_message('Invalid dates input!')
