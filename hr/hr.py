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
                    "Update info about employee.",
                    "Get list of the oldest employees",
                    "Get List of closest to average age"]

    display_menu = True
    while display_menu is True:
        table = create_table_from_file()
        ui.print_menu("Human Resources", list_options, exit_message)
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
            names_of_oldest = get_oldest_person(table)
            ui.print_result(names_of_oldest, "List of the oldest people")

        elif user_choice[0] == "6":

            names_of_closest = get_persons_closest_to_average(table)
            ui.print_result(names_of_closest, "List of closest to average age")

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
    try:
        title_list = ["id", "Name and Surname", "Year of birth"]
        ui.print_table(table, title_list)
    except TypeError:
        ui.print_error_message("No data to show!")


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

    if is_date_number is True and len(data_input[1]) == 4:
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
    if os.path.exists(file_name):
        table = data_manager.get_table_from_file(file_name)

    else:
        ui.print_error_message("There is no file to read!")
        table = []

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


def write_to_file(table):

    full_path = os.getcwd()
    file_name = full_path + "/hr/persons.csv"
    if os.path.exists('persons.csv'):
        data_manager.write_table_to_file(file_name, table)
    else:
        ui.print_error_message("There is no such file!")


def convert_to_int(table):
    """
    Function converts date written in string to integer.

    Args:
        table: list of records

    Returns:
            table with converted data
    """

    for i in range(len(table)):
        table[i][2] = int(table[i][2])

    return table


def sort_table_by_age(table):
    """
    Function uses the bubble sort algorithm to find the oldest persons.

    Args:
        table: list of records to sort

    Returns:
        sorted table
    """
    table = convert_to_int(table)

    for i in range(len(table)-1):

        for j in range(len(table) - 1 - i):

            if table[j][2] < table[j + 1][2]:
                temp_name = table[j][0]

                table[j][2], table[j + 1][2] = table[j + 1][2], table[j][2]
                table[j][1], table[j + 1][1] = table[j + 1][1], table[j][1]
                table[j][0], table[j + 1][0] = table[j + 1][0], table[j][0]
    return(table)
# special functions:
# ------------------


# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    """
    Function checks who is the oldest person on the list

    Args:
        table: list of records

    Returns:
            names_of_oldest: list with names of the oldest
    """

    table = sort_table_by_age(table)

    oldest_birth_year = table[-1][2]

    oldest_name = table[-1][1]
    table.pop(-1)

    names_of_oldest = []
    names_of_oldest.append(oldest_name)

    table_length = len(table) - 1

    for i in range(table_length, -1, -1):

        if table[i][2] == oldest_birth_year:
            names_of_oldest.append(table[i][1])
            table.pop(i)

    return names_of_oldest


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    """
    Function checks who is the person with age closest to the avg. age

    Args:
        table: list of records

    Returns:
            names_of_closest: list with names
    """
    table = sort_table_by_age(table)
    diff_age = calculate_avg_age(table)
    table = sort_table_by_difference(diff_age)

    closest_age = table[-1][0]

    closest_name = table[-1][1]
    table.pop(-1)

    names_of_closest = []
    names_of_closest.append(closest_name)

    table_length = len(table) - 1

    for i in range(table_length, -1, -1):

        if table[i][0] == closest_age:
            names_of_closest.append(table[i][1])
            table.pop(i)

    return names_of_closest


def calculate_avg_age(table):
    """
    Function calculate average age of employees and difference
    beetween age of each person and average age.

    Args:
        table: list of names and age

    Returns:
            diff_age(int):difference beetween age of each person and average age.
    """
    age_of_person_list = []
    age_sum = 0

    for i in range(len(table)):

        age = [2017 - table[i][2], table[i][1]]
        age_of_person_list.append(age)
        age_sum += age_of_person_list[i][0]

    average_age = age_sum / len(age_of_person_list)

    diff_age = []

    for i in range(len(age_of_person_list)):

        difference = average_age - age_of_person_list[i][0]
        if difference < 0:
            difference = difference * -1
        name = age_of_person_list[i][1]
        name_and_difference = [difference, name]
        diff_age.append(name_and_difference)

    return diff_age


def sort_table_by_difference(table):
    """
    Function uses the bubble sort algorithm to find the closest to
    average age persons.

    Args:
        table: list of records to sort

    Returns:
        sorted table
    """

    for i in range(len(table)-1):

        for j in range(len(table) - 1 - i):

            if table[j][0] < table[j + 1][0]:
                temp_name = table[j][0]

                table[j][1], table[j + 1][1] = table[j + 1][1], table[j][1]
                table[j][0], table[j + 1][0] = table[j + 1][0], table[j][0]

    return(table)
