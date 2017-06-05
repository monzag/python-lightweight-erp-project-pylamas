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

    exit_message = "5.Back to main menu."

    list_options = ["1.Show list of employees.",
                    "2.Add new employee.",
                    "3.Remove ann employee by id."
                    "4.Update info about employee."]

    ui.print_menu("Human Resources", list_options, exit_message)
    user_choice = ui.get_inputs(["Menu number"], "Select action by menu number")

    if user_choice[0] == "1":
         table = get_file_path




def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

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


def get_file_path():
    """
    Gets the file path and read the .csv file

    Returns:
            table
    """

    full_path = os.path.abspath()
    file_name = full_path + "/hr/persons.csv"
    table = data_manager.get_table_from_file(file_name)

    return table


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

