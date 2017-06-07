# data structure:
# id: string
#   Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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

    list_options = ["Show list of employees.",
                    "Add new employee.",
                    "Remove record by id",
                    "Update info about employee."]

    display_menu = True
    while display_menu is True:
        table = create_table_from_file()
        ui.print_menu("Human Resources", list_options, exit_message)
        user_choice = ui.get_inputs(["Menu number: "], "Select action by menu number")
        if user_choice[0] == "1":
            show_table(table)

        elif user_choice[0] == "2":
            table = add(table)

        elif user_choice[0] == "3":
            show_table(table)
            id_ = ui.get_inputs(["Id: "], "Type id of record to remove")
            table = remove(table, id_)

        elif user_choice[0] == "4":
            id_ = ui.get_inputs(["Id: "], "Type id of record to change")
            table = update(table, id_)
            show_table(table)

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
    title_list = ["id", "Name and Surname", "Year of birth"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    list_labels = ["Name and Surname: ", "Year of birth(yyyy): "]
    data_input = ui.get_inputs(list_labels, "Add new record")

    id_ = common.generate_random(table)
    is_date_number = data_input[1].isdigit()

    if is_date_number is True and len(data_input) == 4:
        data_input.insert(0, id_)
        table.append(data_input)
    else:
        ui.print_error_message("Wrong year format! Record add failed!")

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
        is_date_number = new_data[0].isdigit()
        if option == 1 or (option == 2 and is_date_number is True and len(new_data[0]) == 4):
            common.insert_new_data(record, new_data[0], option)
        else:
            ui.print_error_message("Wrong year format! Record update failed!")

    return table


def create_table_from_file():
    """
    Gets the file path and read the .csv file

    Returns:
            table
    """

    full_path = os.getcwd()
    file_name = full_path + "/hr/persons.csv"
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
    list_options = ["Name:",
                    "Year:"]

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

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
