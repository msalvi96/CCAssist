""" GA Calling Campaign Assist Module """

import os
from time import sleep
import pandas as pd
from email_updates import main_email

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

def simple_function(row):
    """ Function to print data row """

    reference = row["Ref"]
    first_name = row["First"]
    last_name = row["Last"]
    daytime = row["Daytime"]
    mobile = row["Mobile"]
    citizenship = row["Citizenship1"]

    pretty_print(f"Slate Reference: {reference}", "-")
    pretty_print(f"Name: {first_name} {last_name}", "-")
    pretty_print(f"Contact Numbers: {daytime} / {mobile}", "-")
    pretty_print(f"Citizenship: {citizenship}", "-")

def call_result(called, not_answered, declines):
    """ Function to update call result """

    pretty_print("How was your call?", "*")
    pretty_print("If you talked to the student enter: 200", "-")
    pretty_print("If the call was not answered enter: 500", "-")
    pretty_print("If you did not call the person enter: 999", "-")
    pretty_print("If the student wants to Decline/Withdraw application enter: 404", "-")

    again = True
    while again:
        result = get_int_input()
        if result == 200:
            called += 1
            again = False

        elif result == 500:
            not_answered += 1
            again = False

        elif result == 999:
            again = False

        elif result == 404:
            declines += 1
            again = False

        else:
            print("You can't get out of this! Enter a valid number!")

    return called, not_answered, declines, result

def looping(again):
    """ Function to loop again """

    pretty_print("To Exit enter: 101", ":")
    pretty_print("To continue press any number key:", ":")
    decision = get_int_input()

    if decision == 101:
        again = False

    return again

def ga_assist_main():
    """ Main GA Assist Function """

    clear()
    pretty_print("Hi GAs! Hope you enjoy Calling Campaigns from now", "#")
    ga_name = input("Enter your Name: \n")
    called = 0
    not_answered = 0
    declines = 0
    again = True

    try:
        name = get_file()

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        ga_assist_main()

    else:
        try:
            dataframe = pd.read_excel(name)
            col = list(dataframe)

            called_list = []
            not_called_list = []
            decline_list = []
            no_answer_list = []

            for index, row in dataframe.iterrows():
                row_list = []
                for col_name in col:
                    row_list.append(row[col_name])

                if again:

                    pretty_print(f"Index: {index + 1} / Called: {called} / Not Answered: {not_answered} / Declines: {declines}", "/")
                    simple_function(row)
                    called, not_answered, declines, result = call_result(called, not_answered, declines)

                    if result == 200:
                        called_list.append(row_list)

                    if result == 500:
                        no_answer_list.append(row_list)

                    if result == 999:
                        not_called_list.append(row_list)

                    if result == 404:
                        decline_list.append(row_list)

                    again = looping(again)
                    clear()

                if not again:
                    not_called_list.append(row_list)

            not_called = len(not_called_list)
            total = called + not_answered + declines
            pretty_print("To send Email updates press: 200", "*")
            pretty_print("To continue press any number key:", "*")
            choice = get_int_input()

            if choice == 200:

                try:
                    main_email(ga_name, total, called, not_answered, declines, not_called)
                except Exception as log_error:
                    pretty_print("Server error...Couldn't send the email updates", ":")
                    print(log_error)

            if len(not_called_list) != 0:
                not_called_df = pd.DataFrame(not_called_list, columns=col)
                not_called_df.to_excel(f"{ga_name}-not-called.xlsx", index=False)
                pretty_print(f"Excel File with Not Called Students Data Saved as {ga_name}-not-called.xlsx", "-")

            if len(called_list) != 0:
                called_df = pd.DataFrame(called_list, columns=col)
                called_df.to_excel(f"{ga_name}-called.xlsx", index=False)
                pretty_print(f"Excel File with Called Students Data Saved as {ga_name}-called.xlsx", "-")

            if len(no_answer_list) != 0:
                no_answer_df = pd.DataFrame(no_answer_list, columns=col)
                no_answer_df.to_excel(f"{ga_name}-no-answer.xlsx", index=False)
                pretty_print(f"Excel File with No Answers Saved as {ga_name}-no-answer.xlsx", "-")

            if len(decline_list) != 0:
                decline_df = pd.DataFrame(decline_list, columns=col)
                decline_df.to_excel(f"{ga_name}_declines.xlsx", index=False)
                pretty_print(f"Excel File with Declines saved as {ga_name}_declines.xlsx", "-")

            pretty_print("Have a Nice Day! - @MrunalSalvi", "&")
            sleep(5)

        except Exception as log_error:
            print("Oops something went wrong...")
            print(log_error)
            sleep(10)
