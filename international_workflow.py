""" Internation Workflow Module """

import os
from time import sleep
from prettytable import PrettyTable
import pandas as pd
from models import International
from utils import get_file, get_file_name, pretty_print, clear, get_int_input

class InternationalWorkflow:
    """ Class for International Student Data Filter Workflow """

    def __init__(self, name):
        self.name = name
        self.excel = International(self.name)

        self.main_function_dict = {
            111: self.enrollment_options_filter,
            222: self.enrollment_status_filter,
            333: self.bin_filter,
            444: self.citizenship_filter,
            555: self.decline_filter,
            666: self.school_filter,
            777: self.defer_filter,
            888: self.reporting_filter,
            999: self.on_campus_filter,
            909: self.i20_filter,
            1500: self.calling_campaign,
            101: self.save_quit
        }

        self.main_print_list = [
            ["Enrollment Options Filter", 111, "Enrollment Status Filter", 222],
            ["Bin Filter", 333, "Citizenship Filter", 444],
            ["Decline Filter", 555, "School Filter", 666],
            ["Defer Filter", 777, "Reporting Classification Filter", 888],
            ["On Campus Filter", 999, "I-20 Filter", 909]
        ]

        self.international_table = PrettyTable()
        self.international_table.field_names = ["Options-1", "Commands-1", "Options-2", "Commands-2"]
        for row in self.main_print_list:
            self.international_table.add_row(row)

        self.i20issued_function_dict = {
            111: self.deposit_filter,
            222: self.coa_filter,
            1500: self.calling_campaign,
            101: self.save_quit
        }

        self.i20issued_print_list = [
            ["Deposit Filter", 111],
            ["COA Filter", 222]
        ]

        self.i20NotIssued_function_dict = {
            111: self.transfer_filter,
            222: self.fellowship_filter,
            333: self.deposit_filter,
            1500: self.calling_campaign,
            101: self.save_quit
        }

        self.i20NotIssued_print_list = [
            ["Transfer Filter", 111],
            ["Fellowship Filter", 222],
            ["Deposit Filter", 333]            
        ]

        self.i20Issued_table = PrettyTable()
        self.i20Issued_table.field_names = ["Options", "Commands"]
        for row in self.i20issued_print_list:
            self.i20Issued_table.add_row(row)

        self.i20NotIssued_table = PrettyTable()
        self.i20NotIssued_table.field_names = ["Options", "Commands"]
        for row in self.i20NotIssued_print_list:
            self.i20NotIssued_table.add_row(row)

        self.again = True
        while self.again:
            self.display_ui()

    def display_ui(self):
        for log in self.excel.stack:
            pretty_print(log, "/")

        print(self.international_table)
        pretty_print("Enter Command Number for your Filter of Choice", "-")
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

        except ValueError as e:
            print(e)
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
            sleep(5)
            clear()


    def save_quit(self):
        """ Function to save and quit """

        file_name = get_file_name()
        self.excel.save(file_name)
        for log in self.excel.stack:
            pretty_print(log, "/")

        pretty_print(f"File Saved as {file_name}_(date).xlsx", ":")
        raise SystemExit

    def enrollment_options_filter(self):
        """ Function to filter through enrollment options """

        pretty_print("ENROLLMENT OPTIONS FILTER", "*")
        pretty_print("For filtering through Masters/Graduate Certificate Applications press : 1", "-")
        pretty_print("For filtering through PhD Applications press: 2", "-")
        pretty_print("For Filtering through all applications press any key:", "-")
        enrollment_options = get_int_input()
        self.excel.enrollment_options(enrollment_options)

    def enrollment_status_filter(self):
        """ Function to filter through enrollment status """

        pretty_print("ENROLLMENT STATUS FILTER", "*")
        pretty_print("For Full-Time student data press : 1", "-")
        pretty_print("For Part-Time student data press: 2", "-")
        pretty_print("For all student data press any key:", "-")
        enrollment_status = get_int_input()
        self.excel.enrollment_info(enrollment_status)

    def bin_filter(self):
        """ Function to filter through bin """

        pretty_print("BIN FILTER", "*")
        pretty_print("To access Admits/Conditional Admits press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        bin_options = get_int_input()
        self.excel.admitted_info(bin_options)

    def citizenship_filter(self):
        """ Function to filter through citizenship """

        pretty_print("CITIZENSHIP FILTER", "*")
        pretty_print("For Non-China Citizenship Info press: 1", "-")
        pretty_print("For Chinese Citizenship Info press: 2", "-")
        pretty_print("To continue press any number key:", "-")
        citizenship_options = get_int_input()
        self.excel.citizenship_info(citizenship_options)

    def decline_filter(self):
        """ Function to filter through declines """

        pretty_print("DECLINE FILTER", "*")
        pretty_print("To exclude Declined Applications press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        decline_options = get_int_input()
        self.excel.declines_info(decline_options)

    def school_filter(self):
        """ Function to filter through school """

        pretty_print("SCHOOL FILTER", "*")
        pretty_print("To get SOB Applications press: 1", "-")
        pretty_print("To get SES Applications press: 2", "-")
        pretty_print("To get SSE Applications press: 3", "-")
        pretty_print("To continue press any number key:", "-")
        school_options = get_int_input()
        self.excel.school_info(school_options)

    def defer_filter(self):
        """ Function to filter through deferrals """

        pretty_print("DEFER FILTER", "*")
        pretty_print("To include deferred applications to a specific term press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        defer_options = get_int_input()

        if defer_options == 1:
            string = input('Enter the term: Format - Fall 2019 \n')
            self.excel.deferral_info(string)

    def reporting_filter(self):
        """ Function to filter through reporting classifications """

        pretty_print("REPORTING CLASSIFICATION FILTER", "*")
        pretty_print("For International Reporting Classification press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        reporting_options = get_int_input()
        self.excel.reporting_info(reporting_options)

    def on_campus_filter(self):
        """ Function to filter through on-campus data """

        pretty_print("ON CAMPUS FILTER", "*")
        pretty_print("To filter through On Campus Student Data press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        on_campus_options = get_int_input()
        self.excel.on_campus_info(on_campus_options)

    def transfer_filter(self):
        """ Function to filter through transfer student data """

        pretty_print("TRANSFER FILTER", "*")
        pretty_print("To *delete* Transfer Student Data press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        transfer_options = get_int_input()
        self.excel.transfer_info(transfer_options)

    def fellowship_filter(self):
        """ Function to filter through student fellowship data """

        pretty_print("FELLOWSHIP FILTER", "*")
        pretty_print("To *delete* Students with Fellowships press: 1", "-")
        pretty_print("To continue press any number key:", "-")
        fellowship_options = get_int_input()
        self.excel.fellowship_info(fellowship_options)

    def deposit_filter(self):
        """ Function to filter through deposit paid or not paid """

        pretty_print("DEPOSIT FILTER", "*")
        pretty_print("To include students who have not paid deposit press: 1", "-")
        pretty_print("To include students who have paid the deposit press: 2", "-")
        pretty_print("To continue press any number key:", "-")

        deposit_options = get_int_input()
        self.excel.deposit_info(deposit_options)

    def coa_filter(self):
        """ Function to filter through students submitted / not submitted COA """

        pretty_print("COA FILTER", "*")
        pretty_print("To access students who have not submitted COA press: 1", "-")
        pretty_print("To access students who have submitted COA and attending Stevens press: 2", "-")
        coa_options = get_int_input()
        self.excel.coa_info(coa_options)

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

            self.excel.compare_date_before(date)
            self.save_quit()

        if index == 2:
            date_input = input("Enter a date: Format MM/DD/YY \n")
            try:
                date = pd.to_datetime(date_input)
            except ValueError:
                print("ERROR: Enter a valid date: Format MM/DD/YY ...")
                return

            self.excel.compare_date_after(date)
            self.save_quit()

        if index == 3:
            pretty_print("Filtering", "_")
            self.excel.no_last_contact()
            self.save_quit()

    def i20_filter(self):
        """ Function to filter through I-20 Options """

        pretty_print("I-20 FILTER", "*")
        pretty_print("To access students with no I20 press: 1", "-")
        pretty_print("To access students with I20 issued press: 2", "-")
        i20_options = get_int_input()
        i20_issued = self.excel.i20_info(i20_options)

        if not i20_issued:
            clear()
            again = True
            que_len = len(self.excel.stack)
            while again:
                for log in self.excel.stack:
                    pretty_print(log, "/")

                print(self.i20NotIssued_table)
                pretty_print("Enter Command Number for your Filter of Choice", "-")
                pretty_print("For Calling Campaign Filters enter: 1500", "-")
                pretty_print("To Save and Quit enter: 101", "-")
                pretty_print("To Return to Main Screen enter any number key", "-")
                choice = get_int_input()

                if choice == 101 and len(self.excel.stack) == 0:
                    raise ValueError

                if choice in self.i20NotIssued_function_dict.keys():
                    self.i20NotIssued_function_dict[choice]()

                else:
                    again = False

                if (len(self.excel.stack) - que_len) >= 3:
                    again = False

                clear()

        if i20_issued:
            clear()
            again = True
            que_len = len(self.excel.stack)
            while again:
                for log in self.excel.stack:
                    pretty_print(log, "/")

                print(self.i20Issued_table)
                pretty_print("Enter Command Number for your Filter of Choice", "-")
                pretty_print("For Calling Campaign Filters enter: 1500", "-")
                pretty_print("To Save and Quit enter: 101", "-")
                pretty_print("To Return to Main Screen enter any number key", "-")
                choice = get_int_input()

                if choice == 101 and len(self.excel.stack) == 0:
                    raise ValueError

                if choice in self.i20issued_function_dict.keys():
                    self.i20issued_function_dict[choice]()

                else:
                    again = False

                if (len(self.excel.stack) - que_len) >= 2:
                    again = False

                clear()

def main_international():
    """ International Workflow Main Function """

    pretty_print("International Calling Campaign Filters", "#")
    try:
        file_name = get_file()

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(2)
        main_international()

    InternationalWorkflow(file_name)
