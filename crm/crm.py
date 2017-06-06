# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    file_path = os.getcwd() + '/crm/customers.csv'
    table = get_archive(file_path)

    title = 'Customer relationship management'
    list_options = ['Show subscribers',
                    'Add subscriber',
                    'Remove subscriber',
                    'Update data of subscriber']
    exit_message = 'Back to main menu'

    menu = True
    while menu != '0':
        ui.print_menu(title, list_options, exit_message)
        menu = ui.get_inputs([''], 'Choose action')[0]

        if menu == '1':
            show_table(table)
        elif menu == '2':
            add(table)
        elif menu == '3':
            id_ = ui.get_inputs([''], 'Write id: ')
            table = remove(table, id_)
            show_table(table)
        elif menu == '4':
            id_ = ui.get_inputs([''], 'Write id: ')
            id_ = id_[0]
            update(table, id_)

        elif menu == '0':
            data_manager.write_table_to_file(file_path, table)
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

    title_list = ['id', 'name', 'e-mail', 'newsletter? (yes = 1 / no = 0)']
    ui.print_table(table, title_list)


def get_archive(file_path):
    if os.path.exists(file_path):
        table = data_manager.get_table_from_file(file_path)
    else:
        table = []

    return table


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    list_labels = ['name: ', 'e-mail: ', 'newsletter? (yes = 1 / no = 0): ']
    new_record = ui.get_inputs(list_labels, 'Please provide information about subscriber')

    email = new_record[1]
    newsletter = new_record[2]

    if is_email_valid(email) and is_newsletter_valid(newsletter):
        id_ = common.generate_random(table)
        new_record.insert(0, id_)
        table.append(new_record)

    else:
        ui.print_error_message('Invalid input format.\nYour record will not be added.')

    return table


def is_email_valid(email):
    '''Check that @ occur in email
    If not: false'''

    if '@' in email:
        return True
    else:
        return False


def is_newsletter_valid(newsletter):
    '''Check that user write 1 or 0.
    If something else: False'''

    if newsletter == '1' or newsletter == '0':
        return True
    else:
        return False


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
    common.remove_record(table, record)

    return table


def item_to_change():
    '''Open menu with options, user choose which element should be change.
    Index this element in list is 'options'
    Use in update'''

    title = 'What do you want to change? '
    list_options = ['name ',
                    'e-mail ',
                    'newsletter? (yes = 1 / no = 0): ']
    exit_message = 'Back to main menu'
    ui.print_menu(title, list_options, exit_message)
    inputs = ui.get_inputs([''], 'Choose option')
    option = int(inputs[0])

    return option


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
    option = item_to_change()

    # range of options
    first_option = 1
    last_option = 3

    if option in range(first_option, last_option+1):
        new_data = ui.get_inputs([''], 'Please write new data')[0]

        # check condition for name or email or newsletter
        if option == 1 or is_email_valid(new_data) or is_newsletter_valid(new_data):
            common.insert_new_data(record, new_data, option)

        else:
            ui.print_error_message('Invalid input format.\nYour record will not be added.')

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
