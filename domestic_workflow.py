""" Domestic Workflow Module """

import os
from time import sleep
import pandas as pd
from prettytable import PrettyTable
from models import Domestic

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

def get_file_name():
    """ Function to get file name """

    file_name = input("Enter the name of the output file:\n")
    return file_name

def save_quit(excel, queue):
    """ Function to save and quit """

    file_name = get_file_name()
    excel.save(file_name)
    for log in queue:
        pretty_print(log, "/")

    pretty_print(f"File Save as {file_name}_(date).xlsx", ":")

    raise SystemExit

def get_file():
    """ Function to get input file """

    name = input("Enter Name of the File:\n")
    name = name + ".xlsx"
    os.chdir(os.getcwd())
    if not os.path.exists(name):
        raise FileNotFoundError

    return name

def clear():
    """ Function to clear screen """

    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

def enrollment_options_filter(excel, queue):
    """ Function to filter through enrollment options """

    pretty_print("ENROLLMENT OPTIONS FILTER", "*")
    pretty_print("For filtering through Masters/Graduate Certificate Applications press : 1", "-")
    pretty_print("For filtering through PhD Applications press: 2", "-")
    pretty_print("For Filtering through all applications press any key:", "-")
    enrollment_options = get_int_input()

    if enrollment_options == 1:
        excel.master()
        queue.append("Masters/Graduate Certificate")

    if enrollment_options == 2:
        excel.doctoral()
        queue.append("PhD")


def enrollment_status_filter(excel, queue):
    """ Function to filter through enrollment status"""

    pretty_print("ENROLLMENT STATUS FILTER", "*")
    pretty_print("For Full-Time student data press : 1", "-")
    pretty_print("For Part-Time student data press: 2", "-")
    pretty_print("For all student data press any key:", "-")

    enrollment_status = get_int_input()

    if enrollment_status == 1:
        excel.full_time()
        queue.append("Full Time")

    if enrollment_status == 2:
        excel.part_time()
        queue.append("Part Time")

def calling_campaign(excel, queue):
    """ Function for Calling Campaign Filters """

    pretty_print("CALLING CAMPAIGN FILTER", "*")
    pretty_print("To access data BEFORE last contact date: 1", "-")
    pretty_print("To access data AFTER last contact date press: 2", "-")
    pretty_print("To access data with no last contact date press: 3", "-")

    index = get_int_input()

    if index == 1:
        queue.append("BEFORE last contact date")
        date_input = input("Enter a date: Format MM/DD/YY \n")
        try:
            date = pd.to_datetime(date_input)
        except ValueError:
            print("ERROR: Enter a valid date: Format MM/DD/YY ...")
            queue.append("ERROR: BEFORE last contact date")
            return

        pretty_print("Filtering", "_")
        excel.compare_date_before(date)
        save_quit(excel, queue)

    if index == 2:
        queue.append("AFTER last contact date")
        date_input = input("Enter a date: Format MM/DD/YY \n")
        try:
            date = pd.to_datetime(date_input)
        except ValueError:
            print("ERROR: Enter a valid date: Format MM/DD/YY ...")
            queue.append("ERROR: AFTER last contact date")
            return

        pretty_print("Filtering", "_")
        excel.compare_date_after(date)
        save_quit(excel, queue)

    if index == 3:
        queue.append("No Last Contact Date")
        excel.no_last_contact()
        save_quit(excel, queue)

def main_domestic():
    """ Domestic Workflow Main Function """

    clear()
    pretty_print("Domestic Calling Campaign Filters", "#")

    queue = []

    function_dict = {
        111: enrollment_options_filter,
        222: enrollment_status_filter,
        1500: calling_campaign,
        101: save_quit
    }

    print_list = [
        ["Enrollment Options Filter", 111],
        ["Enrollment Status Filter", 222],
        ["Calling Campiagn Filter", 1500]
    ]

    try:
        name = get_file()
        excel = Domestic(name)

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_domestic()

    again = True
    domestic_table = PrettyTable()
    domestic_table.field_names = ["Options", "Command"]
    for row in print_list:
        domestic_table.add_row(row)

    while again:
        for log in queue:
            pretty_print(log, "/")

        print(domestic_table)
        pretty_print("Choose an option from the Column and enter the corresponding command", "-")
        pretty_print("For Calling Campaign Filters enter: 1500", "-")

        if len(queue) != 0:
            pretty_print("To Save and Quit enter: 101", "-")

        choice = get_int_input()

        try:
            if choice == 101 and len(queue) == 0:
                raise ValueError

            function_dict[choice](excel, queue)
            clear()

        except KeyError:
            pretty_print("Please enter a valid input number.", ":")
            sleep(3)
            again = True
            clear()

        except ValueError:
            pretty_print("You have not applied any filters yet.", ":")
            sleep(3)
            again = True
            clear()

        except IndexError:
            pretty_print("Check data file", ":")
            sleep(3)
            again = True
            clear()

        except SystemExit:
            again = False
            pretty_print("Have a Nice Day! - @MrunalSalvi", "&")
            sleep(5)

        except Exception as log_error:
            again = False
            pretty_print("Oops something went wrong", ":")
            print(log_error)
            sleep(10)
            clear()
