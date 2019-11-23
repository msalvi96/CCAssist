""" Internation Workflow Module """

import os
from time import sleep
from prettytable import PrettyTable
import pandas as pd
from models import International

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

    pretty_print(f"File Saved as {file_name}_(date).xlsx", ":")

    raise SystemExit

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
    """ Function to filter through enrollment status """

    pretty_print("ENROLLMENT STATUS FILTER", "*")
    pretty_print("For Full-Time student data press : 1", "-")
    pretty_print("For Part-Time student data press: 2", "-")
    pretty_print("For all student data press any key:", "-")
    enrollment_status = get_int_input()

    if enrollment_status == 1:
        excel.full_time_international()
        queue.append("Full Time")

    if enrollment_status == 2:
        excel.part_time_international()
        queue.append("Part Time")

def bin_filter(excel, queue):
    """ Function to filter through bin """

    pretty_print("BIN FILTER", "*")
    pretty_print("To access Admits/Conditional Admits press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    bin_options = get_int_input()

    if bin_options == 1:
        excel.admitted_bin()
        queue.append("Admits/Conditional Admits")

def citizenship_filter(excel, queue):
    """ Function to filter through citizenship """

    pretty_print("CITIZENSHIP FILTER", "*")
    pretty_print("For Non-China Citizenship Info press: 1", "-")
    pretty_print("For Chinese Citizenship Info press: 2", "-")
    pretty_print("To continue press any number key:", "-")
    citizenship_options = get_int_input()

    if citizenship_options == 1:
        excel.citizenship_non_china()
        queue.append("Non-China")

    if citizenship_options == 2:
        excel.citizenship_china()
        queue.append("China")

def decline_filter(excel, queue):
    """ Function to filter through declines """

    pretty_print("DECLINE FILTER", "*")
    pretty_print("To exclude Declined Applications press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    decline_options = get_int_input()

    if decline_options == 1:
        excel.no_declines()
        queue.append("Declines Removed")

def school_filter(excel, queue):
    """ Function to filter through school """

    pretty_print("SCHOOL FILTER", "*")
    pretty_print("To get SOB Applications press: 1", "-")
    pretty_print("To get SES Applications press: 2", "-")
    pretty_print("To get SSE Applications press: 3", "-")
    pretty_print("To continue press any number key:", "-")
    school_options = get_int_input()

    if school_options == 1:
        excel.school('SOB')
        queue.append("SOB")

    if school_options == 2:
        excel.school('SES')
        queue.append("SES")

    if school_options == 3:
        excel.school('SSE')
        queue.append("SSE")

def defer_filter(excel, queue):
    """ Function to filter through deferrals """

    pretty_print("DEFER FILTER", "*")
    pretty_print("To include deferred applications to a specific term press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    defer_options = get_int_input()

    if defer_options == 1:
        string = input('Enter the term: Format - Fall 2019 \n')
        excel.defer(string)
        queue.append(f"Defered to {string}")

def reporting_filter(excel, queue):
    """ Function to filter through reporting classifications """

    pretty_print("REPORTING CLASSIFICATION FILTER", "*")
    pretty_print("For International Reporting Classification press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    reporting_options = get_int_input()

    if reporting_options == 1:
        excel.reporting()
        queue.append("Reporting Classification - Int")

def on_campus_filter(excel, queue):
    """ Function to filter through on-campus data """

    pretty_print("ON CAMPUS FILTER", "*")
    pretty_print("To filter through On Campus Student Data press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    on_campus_options = get_int_input()

    if on_campus_options == 1:
        excel.on_campus()
        queue.append("On Campus")

def transfer_filter(excel, queue):
    """ Function to filter through transfer student data """

    pretty_print("TRANSFER FILTER", "*")
    pretty_print("To *delete* Transfer Student Data press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    transfer_options = get_int_input()

    if transfer_options == 1:
        excel.no_transfer()
        queue.append("No Transfers")

def fellowship_filter(excel, queue):
    """ Function to filter through student fellowship data """

    pretty_print("FELLOWSHIP FILTER", "*")
    pretty_print("To *delete* Students with Fellowships press: 1", "-")
    pretty_print("To continue press any number key:", "-")
    fellowship_options = get_int_input()

    if fellowship_options == 1:
        excel.no_fellowship()
        queue.append("No Fellowships")

def deposit_filter(excel, queue):
    """ Function to filter through deposit paid or not paid """

    pretty_print("DEPOSIT FILTER", "*")
    pretty_print("To include students who have not paid deposit press: 1", "-")
    pretty_print("To include students who have paid the deposit press: 2", "-")
    pretty_print("To continue press any number key:", "-")

    deposit_options = get_int_input()

    if deposit_options == 1:
        excel.no_deposit()
        queue.append("No Deposit")

    if deposit_options == 2:
        excel.yes_deposit()
        queue.append("Deposit Paid")

def coa_filter(excel, queue):
    """ Function to filter through students submitted / not submitted COA """

    pretty_print("COA FILTER", "*")
    pretty_print("To access students who have not submitted COA press: 1", "-")
    pretty_print("To access students who have submitted COA and attending Stevens press: 2", "-")
    coa_options = get_int_input()

    if coa_options == 1:
        excel.no_coa()
        queue.append("Not submitted COA")

    if coa_options == 2:
        excel.yes_coa()
        queue.append("Submitted COA")

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

        excel.compare_date_after(date)
        save_quit(excel, queue)

    if index == 3:
        queue.append("No Last Contact Date")
        pretty_print("Filtering", "_")
        excel.no_last_contact()
        save_quit(excel, queue)

def i20_filter(excel, queue):
    """ Function to filter through I-20 Options """

    pretty_print("I-20 FILTER", "*")
    pretty_print("To access students with no I20 press: 1", "-")
    pretty_print("To access students with I20 issued press: 2", "-")
    i20_options = get_int_input()

    if i20_options == 1:
        excel.no_i20()
        queue.append("No I-20")
        clear()
        function_dict = {
            111: transfer_filter,
            222: fellowship_filter,
            333: deposit_filter,
            1500: calling_campaign,
            101: save_quit
        }

        print_list = [
            ["Transfer Filter", 111],
            ["Fellowship Filter", 222],
            ["Deposit Filter", 333]
        ]

        no_i20_table = PrettyTable()
        no_i20_table.field_names = ["Options", "Command"]
        for row in print_list:
            no_i20_table.add_row(row)

        again = True
        que_len = len(queue)
        while again:
            for log in queue:
                pretty_print(log, "/")

            print(no_i20_table)
            pretty_print("Enter Command Number for your Filter of Choice", "-")
            pretty_print("For Calling Campaign Filters enter: 1500", "-")
            pretty_print("To Save and Quit enter: 101", "-")
            pretty_print("To Return to Main Screen enter any number key", "-")
            choice = get_int_input()

            if choice == 101 and len(queue) == 0:
                raise ValueError

            if choice in function_dict.keys():
                function_dict[choice](excel, queue)

            else:
                again = False

            if (len(queue) - que_len) >= 3:
                again = False

            clear()

    if i20_options == 2:
        excel.yes_i20()
        queue.append("I-20 Issued")

        clear()
        function_dict = {
            111: deposit_filter,
            222: coa_filter,
            1500: calling_campaign,
            101: save_quit
        }

        print_list = [
            ["Deposit Filter", 111],
            ["COA Filter", 222]
        ]

        yes_i20_table = PrettyTable()
        yes_i20_table.field_names = ["Options", "Command"]
        for row in print_list:
            yes_i20_table.add_row(row)

        again = True
        que_len = len(queue)
        while again:
            for log in queue:
                pretty_print(log, "/")

            print(yes_i20_table)
            pretty_print("Enter Command Number for your Filter of Choice", "-")
            pretty_print("For Calling Campaign Filters enter: 1500", "-")
            pretty_print("To Save and Quit enter: 101", "-")
            pretty_print("To Return to Main Screen enter any number key", "-")
            choice = get_int_input()

            if choice == 101 and len(queue) == 0:
                raise ValueError

            if choice in function_dict.keys():
                function_dict[choice](excel, queue)

            else:
                again = False

            if (len(queue) - que_len) >= 2:
                again = False

            clear()

def main_international():
    """International Workflow Main Function """

    clear()
    pretty_print("International Calling Campaign Filters", "#")

    queue = []
    function_dict = {
        111: enrollment_options_filter,
        222: enrollment_status_filter,
        333: bin_filter,
        444: citizenship_filter,
        555: decline_filter,
        666: school_filter,
        777: defer_filter,
        888: reporting_filter,
        999: on_campus_filter,
        909: i20_filter,
        1500: calling_campaign,
        101: save_quit
    }

    print_list = [
        ["Enrollment Options Filter", 111, "Enrollment Status Filter", 222],
        ["Bin Filter", 333, "Citizenship Filter", 444],
        ["Decline Filter", 555, "School Filter", 666],
        ["Defer Filter", 777, "Reporting Classification Filter", 888],
        ["On Campus Filter", 999, "I-20 Filter", 909]
    ]

    try:
        name = get_file()
        excel = International(name)

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_international()

    again = True
    international_table = PrettyTable()
    international_table.field_names = ["Options-1", "Commands-1", "Options-2", "Commands-2"]
    for row in print_list:
        international_table.add_row(row)

    while again:
        for log in queue:
            pretty_print(log, "/")

        print(international_table)
        pretty_print("Enter Command Number for your Filter of Choice", "-")
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

        except ValueError as e:
            print(e)
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
            sleep(5)
            clear()
