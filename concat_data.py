""" Concat Data Module """

import os
from time import sleep
import pandas as pd

def pretty_print(string, design):
    """ Pretty Print Function """

    print(f"  {string}  ".center(100, design))

def get_int_input():
    """ Function to get integer input """

    var_input = input()
    try:
        var_input = int(var_input)
        return var_input
    except ValueError:
        print('ERROR: Enter a Valid Number... \n')
        get_int_input()

def clear():
    """ Function to clear screen """

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def get_file(i):
    """ Function to get input file """

    name = input(f"Enter Name of the File {i}:\n")
    name = name + ".xlsx"
    os.chdir(os.getcwd())
    if not os.path.exists(name):
        raise FileNotFoundError

    return name

def get_file_name():
    """ Function to get file name """

    file_name = input(f"Enter name for Output Excel File:\n")
    return file_name

def concat_ordered_columns(frames):
    """ Function to concat dataframes in list and order them by columns """

    columns_ordered = []
    for frame in frames:
        columns_ordered.extend(x for x in frame.columns if x not in columns_ordered)

    final_df = pd.concat(frames, sort=True)

    return final_df[columns_ordered]

def concat_data_main():
    """ Main Concat Data Function """

    clear()
    pretty_print("You can combine two or more excel files here:", "#")
    pretty_print("How many files do you want to combine:", "-")

    file_list = []

    try:
        number = get_int_input()

        if number <= 1:
            raise ValueError

        if number >= 10:
            raise ArithmeticError

        for i in range(number):
            name = get_file(i)
            data_frame = pd.read_excel(name)
            file_list.append(data_frame)
            clear()

        full_df = concat_ordered_columns(file_list)
        new_name = get_file_name()
        full_df.to_excel(f"{new_name}.xlsx", index=False)
        pretty_print(f"File Saved as {new_name}.xlsx", "-")
        pretty_print("Have a Nice Day! - @Mrunal", "&")
        sleep(5)

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        concat_data_main()

    except ValueError:
        pretty_print("You can't combine a single file or no file... How sad!", ":")
        pretty_print("Try Again!", ":")
        sleep(5)
        concat_data_main()

    except ArithmeticError:
        pretty_print("I can combine more than 10 excel files together but I just don't want to ;-)", ":")
        pretty_print("Try Again", ":")
        sleep(5)
        concat_data_main()

    except Exception as log_error:
        print("Oops something went wrong")
        print(log_error)
        sleep(10)
