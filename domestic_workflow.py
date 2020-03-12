""" Domestic Workflow Module """

import os
from time import sleep
import pandas as pd
from prettytable import PrettyTable
from models import Domestic
from utils import pretty_print, get_int_input, get_file_name, get_file, clear

class DomesticWorkflow:

    def __init__(self, name):
        self.name = name
        self.excel = Domestic(self.name)

        self.main_function_dict = {
            111: self.enrollment_options_filter,
            222: self.enrollment_status_filter,
            1500: self.calling_campaign,
            101: self.save_quit
        }

        self.main_print_list = [
            ["Enrollment Options Filter", 111],
            ["Enrollment Status Filter", 222],
            ["Calling Campiagn Filter", 1500]
        ]

        self.domestic_table = PrettyTable()
        self.domestic_table.field_names = ["Options", "Command"]
        for row in self.main_print_list:
            self.domestic_table.add_row(row)

        self.again = True
        while self.again:
            self.displayUI()

    def save_quit(self):
        """ Function to save and quit """

        file_name = get_file_name()
        self.excel.save(file_name)
        for log in self.excel.stack:
            pretty_print(log, "/")

        pretty_print(f"File Save as {file_name}_(date).xlsx", ":")

        raise SystemExit

    def displayUI(self):
        for log in self.excel.stack:
            pretty_print(log, "/")

        print(self.domestic_table)
        pretty_print("Choose an option from the Column and enter the corresponding command", "-")
        pretty_print("For Calling Campaign Filters enter: 1500", "-")

        if len(self.excel.stack) != 0:
            pretty_print("To Save and Quit enter: 101", "-")

        choice = get_int_input()

        try:
            if choice == 101 and len(self.excel.stack) == 0:
                raise ValueError

            self.main_function_dict[choice]()
            clear()

        except KeyError:
            pretty_print("Please enter a valid input number.", ":")
            sleep(3)
            self.again = True
            clear()

        except ValueError:
            pretty_print("You have not applied any filters yet.", ":")
            sleep(3)
            self.again = True
            clear()

        except IndexError:
            pretty_print("Check data file", ":")
            sleep(3)
            self.again = True
            clear()

        except SystemExit:
            self.again = False
            pretty_print("Have a Nice Day! - @MrunalSalvi", "&")
            sleep(5)

        except Exception as log_error:
            self.again = False
            pretty_print("Oops something went wrong", ":")
            print(log_error)
            sleep(10)
            clear()


    def enrollment_options_filter(self):
        """ Function to filter through enrollment options """

        pretty_print("ENROLLMENT OPTIONS FILTER", "*")
        pretty_print("For filtering through Masters/Graduate Certificate Applications press : 1", "-")
        pretty_print("For filtering through PhD Applications press: 2", "-")
        pretty_print("For Filtering through all applications press any key:", "-")
        enrollment_options = get_int_input()
        self.excel.enrollment_options(enrollment_options)

    def enrollment_status_filter(self):
        """ Function to filter through enrollment status"""

        pretty_print("ENROLLMENT STATUS FILTER", "*")
        pretty_print("For Full-Time student data press : 1", "-")
        pretty_print("For Part-Time student data press: 2", "-")
        pretty_print("For all student data press any key:", "-")

        enrollment_status = get_int_input()
        self.excel.enrollment_info(enrollment_status)

    def calling_campaign(self):
        """ Function for Calling Campaign Filters """

        pretty_print("CALLING CAMPAIGN FILTER", "*")
        pretty_print("To access data BEFORE last contact date: 1", "-")
        pretty_print("To access data AFTER last contact date press: 2", "-")
        pretty_print("To access data with no last contact date press: 3", "-")

        index = get_int_input()

        if index == 1:
            date_input = input("Enter a date: Format MM/DD/YY \n")
            try:
                date = pd.to_datetime(date_input)
            except ValueError:
                print("ERROR: Enter a valid date: Format MM/DD/YY ...")
                return

            pretty_print("Filtering", "_")
            self.excel.compare_date_before(date)
            self.save_quit()

        if index == 2:
            date_input = input("Enter a date: Format MM/DD/YY \n")
            try:
                date = pd.to_datetime(date_input)
            except ValueError:
                print("ERROR: Enter a valid date: Format MM/DD/YY ...")
                return

            pretty_print("Filtering", "_")
            self.excel.compare_date_after(date)
            self.save_quit()

        if index == 3:
            self.excel.no_last_contact()
            self.save_quit()

def main_domestic():
    """ Domestic Workflow Main Function """

    clear()
    pretty_print("Domestic Calling Campaign Filters", "#")
    try:
        name = get_file()

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_domestic()

    DomesticWorkflow(name)
