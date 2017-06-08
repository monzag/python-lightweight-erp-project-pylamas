# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    exit_message = "Back to main menu."

    list_options = ["Show inventory list.",
                    "Add new item.",
                    "Remove record by id",
                    "Update info about item.",
                    "Get list of available items",
                    "Get average durability by manufacturers"]

    display_menu = True
    while display_menu is True:
        table = create_table_from_file()
        ui.print_menu("Inventory", list_options, exit_message)
        user_choice = ui.get_inputs(["Menu number: "], "Select action by menu number")

        if user_choice[0] == "1":
            show_table(table)

        elif user_choice[0] == "2":
            table = add(table)
            write_to_file(table)

        elif user_choice[0] == "3":
            show_table(table)
            id_ = ui.get_inputs(["Id: "], "Type id of record to remove")
            table = remove(table, id_)
            write_to_file(table)

        elif user_choice[0] == "4":
            id_ = ui.get_inputs(["Id: "], "Type id of record to change")
            table = update(table, id_)
            write_to_file(table)
            show_table(table)

        elif user_choice[0] == "5":
            list_of_items = get_available_items(table)
            ui.print_result(list_of_items, "List of available items")

        elif user_choice[0] == "6":
            average_durability = get_average_durability_by_manufacturers(table)
            ui.print_result(average_durability, "Get average durability by manufacturers dctionary")

        elif user_choice[0] == "0":
            display_menu = False


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["id", "Name", "Manufacturer", "Purchase Date", "Durability"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    list_labels = ["Name: ", "Manufacturer: ", "purchase_date: ", "Durability: "]
    data_input = ui.get_inputs(list_labels, "Add new record")

    id_ = common.generate_random(table)
    is_date_number = data_input[2].isdigit() and len(data_input) == 4
    is_durability_number = data_input[3].isdigit()

    if is_date_number is True and is_durability_number is True:
        data_input.insert(0, id_)
        table.append(data_input)
    elif is_date_number is False:
        ui.print_error_message("Wrong year format! Record add failed!")
    elif is_durability_number is False:
        ui.print_error_message("Wrong durability format! Record add failed!")

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

    record = common.find_id(table, id_[0])
    table = common.remove_record(table, record)

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

    record = common.find_id(table, id_[0])
    option, amount_data, data_info = data_to_change()

    if option in range(1, amount_data):
        new_data = ui.get_inputs(["Type " + data_info], 'Please write new data')
        is_date_number = new_data[0].isdigit() and len(new_data[0]) == 4
        is_durability_number = new_data[0].isdigit()

        if option == 1 or option == 2:
            common.insert_new_data(record, new_data[0], option)

        elif option == 3 and is_date_number is True:
            common.insert_new_data(record, new_data[0], option)

        elif option == 4 and is_durability_number is True:
            common.insert_new_data(record, new_data[0], option)

        else:
            ui.print_error_message("Wrong format! Record update failed!")

    return table


def create_table_from_file():
    """
    Gets the file path and read the .csv file

    Returns:
            table
    """

    full_path = os.getcwd()
    file_name = full_path + "/inventory/inventory.csv"
    table = data_manager.get_table_from_file(file_name)
    return table


def data_to_change():
    """
    Gets from user number of option to change, checks amount of options
    and data type.

    Returns:
            option(int): number of option to change
            amount_data(int): amount of all options
            data_info(str): title of data to overwrite
    """

    title = "Which part of record You want to change?"
    exit_message = "Back to main menu."
    list_options = ["Name: ", "Manufacturer: ", "purchase_date: ", "Durability: "]

    ui.print_menu(title, list_options, exit_message)
    correct_input = False
    while correct_input is not True:
        try:
            inputs = ui.get_inputs(['Number'], "Choose data to overwrite.")
            option = int(inputs[0])
            amount_data = len(list_options) + 1
            data_info = list_options[option - 1]
            correct_input = True

        except ValueError:
            ui.print_error_message("Only numbers!")

        else:
            return option, amount_data, data_info


def write_to_file(table):
    full_path = os.getcwd()
    file_name = full_path + "/inventory/inventory.csv"
    data_manager.write_table_to_file(file_name, table)


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    """
    Function checks the durability of items and if they have
    not exceeded appends item to list

    Args:
        table: list of items with info

    Returns:
            list_of_items: list with items that have not exceeded
    """

    list_of_items = []

    for i in range(len(table)):

        table[i][3] = int(table[i][3])
        table[i][4] = int(table[i][4])
        expiration_date = table[i][3] + table[i][4]
        durability = 2017 - expiration_date

        if durability <= 0:
            list_of_items.append(table[i])

    return list_of_items


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):
    """
    Function creates dictionary with manufacturers as keys
    and average durability as items.

    Args:
        table: list with data

    Returns:
            average_durability(dictionary): dictionary key[manufacturer] : item[average durability]
    """

    average_durability = {}

    for i in range(len(table)):
        table[i][4] = int(table[i][4])

    manufacturers = [name[2] for name in table]

    single_manufacturers = list(set(manufacturers))

    for i in range(len(single_manufacturers)):
        durability_sum = 0
        count = 0
        for j in range(len(manufacturers)):
            if single_manufacturers[i] == manufacturers[j]:
                count += 1
                durability_sum += int(table[j][4])
        average_durability[single_manufacturers[i]] = durability_sum / count

    return average_durability
