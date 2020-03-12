import os

def get_int_input():
    """ Function to get integer input """

    var_input = input()
    try:
        var_input = int(var_input)
        return var_input
    except ValueError:
        print('ERROR: Enter a Valid Number... \n')
        get_int_input()

def pretty_print(string, design):
    """ Pretty Print Function """

    print(f"  {string}  ".center(100, design))

def clear():
    """ Function to clear screen """

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def get_file():
    """ Function to get input file """

    name = input("Enter Name of the File:\n")
    name = name + ".xlsx"
    os.chdir(os.getcwd())
    if not os.path.exists(name):
        raise FileNotFoundError

    return name

def get_file_name():
    """ Function to get file name """

    file_name = input("Enter the name of the output file:\n")
    return file_name