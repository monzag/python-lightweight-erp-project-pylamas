

def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """
    MIN_COLUMN_WIDTH = 8
    CELL_PADDING = 2
    columns_number = len(table[0])

    outer_row = create_outer_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING)
    middle_row = create_middle_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING)

    print('◤{}◥'.format(outer_row))
    for i in range(len(table)):  # jak to poprawić?
        title_row = create_data_row(table, i, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=True)
    print(title_row)
    for i in range(len(table)):
        data_row = create_data_row(table, i, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=False)
        print(middle_row)
        print(data_row)
    print('◣{}◢'.format(outer_row))


def create_data_row(table, list_index, title_list, MIN_COLUMN_WIDTH, CELL_PADDING, is_title=False):

    data_row = '|'

    for i in range(len(table[list_index])):
        max_string_length = find_max_string_length(table, i, title_list)
        if max_string_length >= MIN_COLUMN_WIDTH:
            cell_width = max_string_length + CELL_PADDING
        else:
            cell_width = MIN_COLUMN_WIDTH

        if is_title == False:
            data_row = data_row + (table[list_index][i].center(cell_width, ' ')) + '|'
        else:
            data_row = data_row + (title_list[i].center(cell_width, ' ')) + '|'

    return data_row


def create_middle_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING):

    middle_row = '|'

    for i in range(columns_number):
        dashes_to_add = find_max_string_length(table, i, title_list)
        if dashes_to_add >= MIN_COLUMN_WIDTH:
            middle_row = middle_row + ('-' * (dashes_to_add + CELL_PADDING) + '|')
        else:
            middle_row = middle_row + ('-' * MIN_COLUMN_WIDTH + '|')

    return middle_row


def create_outer_row(table, columns_number, title_list, MIN_COLUMN_WIDTH, CELL_PADDING):

    outer_row = ''

    for i in range(columns_number):
        dashes_to_add = find_max_string_length(table, i, title_list)
        if dashes_to_add >= MIN_COLUMN_WIDTH:
            outer_row = outer_row + ('-' * (dashes_to_add + CELL_PADDING))
        else:
            outer_row = outer_row + ('-' * MIN_COLUMN_WIDTH)

    additional_dashes = columns_number - 1
    outer_row = outer_row + ('-' * additional_dashes)

    return outer_row


def find_max_string_length(table, item_index, title_list):
    longest_string = ''

    for a_list in table:
        if len(str(a_list[item_index])) > len(longest_string):
            longest_string = str(a_list[item_index])

    if len(str(title_list[item_index])) > len(longest_string):
        longest_string = str(title_list[item_index])

    longest_value = len(longest_string)

    return longest_value


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # your code

    pass


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """

    option_number = 1

    print('{}:'.format(title))
    for i in list_options:
        print('    ({}) '.format(option_number) + i)
        option_number += 1
    print('    (0) {}'.format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    print('{}:'.format(title))
    for i in list_labels:
        answer = (input('{} '.format(i)))
        inputs.append(answer)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    print(message)

# FOR TESTS:
#title = "Main menu"
#list_options = ['Jedna opcja', 'Druga opcja', 'blabla3423#$@']
#exit_message = "Do widzenia!"
#print_menu(title, list_options, exit_message)

#list_labels = ['Age', 'cos tam']
#title_input = 'Wpisz byle co, bo testujemy'
#print(get_inputs(list_labels, title_input))

table = [['234653633646', '34624256', '4564', '54', '64'], ['656333667734', '34672', '4534', '1sdghe3', '3aassa2'],
['123373441231', '54354', '6346', '42', '32'], ['222539048759', '23424', '4522', '43', '21'],
['1023342423423438743', '23423', '6364', 'fsdfdgdgsdg78', '65']]
title_list = ['jedne dane', 'drugie dane', 'bal', 'lab', 'x']
print_table(table, title_list)
