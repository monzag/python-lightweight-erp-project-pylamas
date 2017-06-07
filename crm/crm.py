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

    table = get_data_from_file()

    title = 'Customer relationship management'
    list_options = ['Show subscribers',
                    'Add subscriber',
                    'Remove subscriber',
                    'Update data of subscriber',
                    'Get the longest name',
                    'Get subscribed e-mail']
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
            id_ = ui.get_inputs([''], 'Write id: ')[0]
            update(table, id_)

        elif menu == '5':
            id_longest_name = get_longest_name_id(table)
            ui.print_result(id_longest_name, 'Id of the longest name')

        elif menu == '6':
            person_newsletter = get_subscribed_emails(table)
            ui.print_result(person_newsletter, 'List of subsribers')

        elif menu == '0':
            save_data_to_file(table)

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


def get_data_from_file():
    '''
    Read data from file - if exists. If not - data is empty list.

    Returns:
        table
    '''
    file_name = os.getcwd() + '/crm/customers.csv'
    if os.path.exists(file_name):
        table = data_manager.get_table_from_file(file_name)
    else:
        table = []

    return table


def save_data_to_file(table):
    """
    Exports data to file using data_manager module

    Args:
        table - list of lists with overwrite data

    Returns:
        None
    """

    file_path = os.getcwd() + '/crm/customers.csv'
    data_manager.write_table_to_file(file_path, table)


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
        save_data_to_file(table)

    else:
        ui.print_error_message('Invalid input format.\nYour record will not be added.')

    return table


def is_email_valid(email):
    '''
    Check that @ occur in email

    Args:
        email - element 2 from record in table

    Return
        True if occur, else: False
    '''

    if '@' in email:
        return True
    else:
        return False


def is_newsletter_valid(newsletter):
    '''
    Check that user write correct number: 1 or 0.

    Args:
        newsletter - element 3 from record in table

    Returns:
        True if proper format, else: False
    '''

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
    save_data_to_file(table)

    return table


def data_to_change():
    '''
    Display menu with options, user choose which element should be change.

    Returns:
        option - users input (number). It means index of element in table.
    '''

    title = 'What do you want to change? '
    list_options = ['name ',
                    'e-mail ',
                    'newsletter? (yes = 1 / no = 0): ']
    exit_message = 'Back to main menu'
    ui.print_menu(title, list_options, exit_message)
    options = ui.get_inputs([''], 'Choose option')
    option = int(options[0])

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
    option = data_to_change()

    # range of options
    first_option = 1
    last_option = 3

    if option in range(first_option, last_option+1):
        new_data = ui.get_inputs([''], 'Please write new data')[0]

        # check condition for name or email or newsletter
        if option == 1 or is_email_valid(new_data) or is_newsletter_valid(new_data):
            common.insert_new_data(record, new_data, option)
            save_data_to_file(table)

        else:
            ui.print_error_message('Invalid input format.\nYour record will not be added.')

    return table


def get_longest_name_id(table):
    '''
    Compare length of names in the table and get id the longest name. 
    If there are more than one longest name, return the first by 'asscending' alphabetical order

    Args:
        table - list in lists where is find element with index 1 (name)

    Returns:
        Id of longest name

    '''
    longest_name = ''
    id_longest_name = ''
    index_name = 1
    index_id = 0

    for row in table:
        name = row[index_name].lower()
        id_ = row[index_id]

        if len(name) > len(longest_name):
            longest_name = name
            id_longest_name = id_

        elif len(name) == len(longest_name):
            longest_name = min(name, longest_name)
            if longest_name == name:
                id_longest_name = id_

    return id_longest_name


def get_subscribed_emails(table):
    '''
    Create new list with customers subscribed to the newsletter.

    Args:
        table: list of lists with specific items

    Returns:
        person_with_newsletter - list of string 'email;name'
    '''
    index_name = 1
    index_email = 2
    index_newsletter = 3
    person_with_newsletter = []

    for row in table:
        if row[index_newsletter] == '1':
            record = row[index_email] + ";" + row[index_name]
            person_with_newsletter.append(record)

    return person_with_newsletter
