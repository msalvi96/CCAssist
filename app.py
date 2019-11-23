""" Calling Campaign Assist Main App File """

from time import sleep
from international_workflow import main_international
from domestic_workflow import main_domestic
from ga_assist import ga_assist_main
from split_data import main_df_split
from concat_data import concat_data_main

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
        print('ERROR: Enter a Valid Number...')
        get_int_input()

def main():
    """ Main App Function """

    pretty_print("Welcome to EXCELSIOR", "#")
    pretty_print("For International Student Data Filters press: 1", "-")
    pretty_print("For Domestic Student Data Filters press: 2", "-")
    pretty_print("To split an excel file in equal parts: 3", "-")
    pretty_print("To combine multiple excel files in a single file press: 4", "-")
    pretty_print("For GA Calling Campaign Assist: 5", "-")
    pretty_print("Press any key to exit the application", "-")

    choice = get_int_input()

    if choice == 1:
        main_international()

    elif choice == 2:
        main_domestic()

    elif choice == 3:
        main_df_split()

    elif choice == 4:
        concat_data_main()

    elif choice == 5:
        ga_assist_main()

    else:
        raise SystemExit

if __name__ == "__main__":

    try:
        main()

    except SystemExit:
        pretty_print("Thanks for nothing", "*")
        sleep(3)
