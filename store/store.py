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
    table = get_data_from_file()
    display_menu(table)
    save_data_to_file(table)


def get_data_from_file():
    """
    Imports data from CSV file into a table
    or returns empty list if file does not exist

    Returns:
        table - list of lists of data
    """
    file_path = os.getcwd() + '/store/games.csv'
    if os.path.exists(file_path):
        table = data_manager.get_table_from_file(file_path)
    else:
        table = []
    return table


def save_data_to_file(table):
    """
    Exports data to file using data_manager module

    Parameters:
        table - list of lists
    Returns:
        None
    """
    file_path = os.getcwd() + '/store/games.csv'
    data_manager.write_table_to_file(file_path, table)


def display_menu(table):
    '''
    Displays the main menu of the module.
    Enables user to perform all the operations.

    Args:
        table: list of lists of data

    Returns:

    '''
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
        elif option == '3':
            get_record_id(table, remove)
        elif option == '4':
            get_record_id(table, update)
        elif option == '5':
            result = get_counts_by_manufacturers(table)
            ui.print_result(result, 'Dictionary of total amount of games by manufacturer')
        elif option == '6':
            result = get_manufacturer_name(table)
            ui.print_result(str(result), 'Average amount of games in stock')
        elif option == '0':
            break
        else:
            ui.print_error_message('Invalid input')


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

    LIST_LABELS = ['Title', 'Manufacturer', 'Price($)', 'Items in stock']
    new_record = ui.get_inputs(LIST_LABELS, 'Add new game')

    id_ = common.generate_random(table)
    money = new_record[2]
    instock = new_record[3]

    if common.is_money_valid(money) is True and instock.isdigit():
        new_record.insert(0, id_)
        table.append(new_record)
    else:
        ui.print_error_message("Wrong number format! Record add failed!")

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


def get_record_id(table, operation):
    """
    Specifies record which user would like to change,
    and determines if it's possible

    Parameters:
        table: list of lists containing data
        operation: str (type of operation to be performed after(update or remove))

    Returns:
        table - list of lists (updated)
    """
    show_table(table)
    id_ = ui.get_inputs([''], 'Type id of record to be {}d'.format(str(operation)))[0]
    ids = [record[0] for record in table]
    if id_ in ids:
        table = operation(table, id_)
    else:
        ui.print_error_message('Invalid id input')
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
    record = common.find_id(table, id_)
    option, amount_options, data_name = data_to_update()

    if option in range(1, amount_options):
        new_data = ui.get_inputs(['{}: '.format(data_name)], 'Please write new data')
        is_number = new_data[0].isdigit()

        if option == 1 or option == 2 or (option == 3 and is_number is True) or (option == 4 and is_number is True):
            common.insert_new_data(record, new_data[0], option)
        else:
            ui.print_error_message("Wrong format! Record update failed!")

    return table


def data_to_update():
    """
    Gets from user number of option to change, checks amount of options
    and data type.

    Returns:
            option(int): number of option to change
            amount_options(int): amount of all options
            data_name(str): title of data to overwrite
    """

    title = "Which part of record do you want to change?"
    exit_message = "Back to main menu."
    list_options = ["Title",
                    "Manufacturer",
                    "Price",
                    "In stock"]

    ui.print_menu(title, list_options, exit_message)

    correct_input = False
    while correct_input is not True:
        try:
            inputs = ui.get_inputs(['Number'], "Choose data to overwrite")
            option = int(inputs[0])
            amount_options = len(list_options) + 1
            data_name = list_options[option - 1]
            correct_input = True

        except ValueError:
            ui.print_error_message("Please enter a number!")

        else:
            return option, amount_options, data_name

# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }


def get_counts_by_manufacturers(table):
    """
    Counts the number of games by each manufacturer.

    Args:
        table: list of lists containing details of each game

    Returns:
        dictionary with manufacturer as a key (str) and games number as a value (int)
        (e.g. {'Blizzard Entertainment' : 3})
        label: string (label of a result)
    """
    counts_by_manufacturers = {}

    for i in table:
        if i[2] not in counts_by_manufacturers:
            counts_by_manufacturers[i[2]] = 1
        elif i[2] in counts_by_manufacturers:
            counts_by_manufacturers[i[2]] += 1

    return counts_by_manufacturers


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_manufacturer_name(table):
    '''
    Asks for a manufacturer name and checks if it exists in database.
    If it exists, launches the get_average_by_manufacturer function
    and returns its result and label.

    Args:
        table: list of lists of data

    Returns:
        result: int (if manufacturer exists) or str (if manufacturer does not exist)
    '''

    manufacturer = ui.get_inputs([''], 'Type manufacturer\'s name to show it\'s average amount of games in stock')[0]

    for record in table:
        if record[2] == manufacturer:
            result = get_average_by_manufacturer(table, manufacturer)
            return result

    result = "There is no such manufacturer in database!"

    return result


def get_average_by_manufacturer(table, manufacturer):
    '''
    Counts the average amount of games by manufacturer available in stock.

    Args:
        table: list of lists with details of each game
        manufacturer: string being contained in any list from the table

    Returns:
        result: float
        label: label of a result
    '''
    games_instock = 0
    games_count = 0

    for i in table:
        if i[2] == manufacturer:
            games_instock += int(i[4])
            games_count += 1

    result = games_instock / games_count

    return result
