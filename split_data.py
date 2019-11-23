""" Split Data Module """

import os
from time import sleep
import numpy as np
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

def get_file():
    """ Function to get input file """

    name = input("Enter Name of the File:\n")
    name = name + ".xlsx"
    os.chdir(os.getcwd())
    if not os.path.exists(name):
        raise FileNotFoundError

    return name

def get_file_name(index):
    """ Function to get file name """

    file_name = input(f"Enter name for Excel File: {index}\n")
    return file_name

def main_df_split():
    """ Main function to split data files """

    clear()
    pretty_print("You can split the file in equal parts here:", "#")

    try:
        name = get_file()
        pretty_print("How many chunks do you need?", "-")
        number = get_int_input()
        data_frame = pd.read_excel(name)
        split_df = np.array_split(data_frame, number)
        for index, dataframe in enumerate(split_df, 1):
            file_name = get_file_name(index)
            dataframe.to_excel(f"{file_name}.xlsx", index=False)
            pretty_print(f"File {index} {file_name}.xlsx Saved", "*")

        pretty_print("Have a Nice Day! - @MrunalSalvi", "&")
        sleep(5)

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_df_split()

    except Exception as log_error:
        print("Oops something went wrong...")
        print(log_error)
        sleep(10)
