# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

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
    file_path = os.getcwd() + '/store/games.csv'
    table = get_archive(file_path)

    title = "Store Manager"
    list_options = ["Show list of games",
               "Add new game",
               "Remove a game by id",
               "Update a game by id",
               "Show amount of games by manufacturer",
               "Show average amount of games by manufacturer"]
    exit_message = "Back to main menu"

    option = None
    while option != '0':
        ui.print_menu(title, list_options, exit_message)
        inputs = ui.get_inputs([''], 'Choose action to perform')
        option = inputs[0]

        if option == '1':
            show_table(table)
        elif option == '2':
            add(table)
            data_manager.write_table_to_file(file_path, table)
        elif option == '3':
            show_table(table)
            table = find_and_remove_record(table)
            data_manager.write_table_to_file(file_path, table)
        elif option == '4':
            update(table, id_)
            data_manager.write_table_to_file(file_path, table)
        elif option == '0':
            break
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

    title_list = ['ID', 'Title', 'Manufacturer', 'Price', 'In stock']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    list_labels = ['Title', 'Manufacturer', 'Price($)', 'Items in stock']
    new_record = ui.get_inputs(list_labels, 'Add new game')

    id_ = common.generate_random(table)
    money = new_record[2]
    instock = new_record[3]

    if common.is_money_valid(money) == True and instock.isdigit():
        new_record.insert(0, id_)
        table.append(new_record)
    else:
        ui.print_error_message("Wrong number format! Record add failed!")

    return table


def get_id_from_user(table):
    id_ = ui.get_inputs([''], 'Type id of record')[0]
    ids = common.get_value_from(table, 0)
    if id_ not in ids:
        ui.print_error_message('There is no record with this id')
    else:
        return id_


def find_and_remove_record(table):
    id_ = get_id_from_user(table)
    if id_ != None:
        table = remove(table, id_)
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

    record = common.find_id(table, id_)
    common.remove_record(table, record)

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

    position = 1
    new_data = 'new_name'
    record = common.find_id(table, id_)
    common.insert_new_data(record, new_data, position)

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    games_by_manufacturers = {}

    

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
