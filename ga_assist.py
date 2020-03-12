""" GA Calling Campaign Assist Module """

import os
from time import sleep
import pandas as pd
from email_updates import main_email
from utils import pretty_print, get_int_input, clear, get_file, get_file_name

class GAassist:

    def __init__(self, ga_name, file_name):
        self.ga_name = ga_name
        self.file_name = file_name

        self.called = 0
        self.not_answered = 0
        self.declines = 0
        self.again = True

        self.called_list = []
        self.not_called_list = []
        self.decline_list = []
        self.no_answer_list = []

        self.excel = pd.read_excel(file_name)
        self.col = list(self.excel)

        for index, row in self.excel.iterrows():
            self.display_row_ui(index, row)

        self.not_called = len(self.not_called_list)
        self.total = self.called + self.not_answered + self.declines

        self.email_options()
        self.save_quit()

    def save_quit(self):

        if len(self.not_called_list) != 0:
            not_called_df = pd.DataFrame(self.not_called_list, columns=self.col)
            not_called_df.to_excel(f"{self.ga_name}-not-called.xlsx", index=False)
            pretty_print(f"Excel File with Not Called Students Data Saved as {self.ga_name}-not-called.xlsx", "-")

        if len(self.called_list) != 0:
            called_df = pd.DataFrame(self.called_list, columns=self.col)
            called_df.to_excel(f"{self.ga_name}-called.xlsx", index=False)
            pretty_print(f"Excel File with Called Students Data Saved as {self.ga_name}-called.xlsx", "-")

        if len(self.no_answer_list) != 0:
            no_answer_df = pd.DataFrame(self.no_answer_list, columns=self.col)
            no_answer_df.to_excel(f"{self.ga_name}-no-answer.xlsx", index=False)
            pretty_print(f"Excel File with No Answers Saved as {self.ga_name}-no-answer.xlsx", "-")

        if len(self.decline_list) != 0:
            decline_df = pd.DataFrame(self.decline_list, columns=self.col)
            decline_df.to_excel(f"{self.ga_name}_declines.xlsx", index=False)
            pretty_print(f"Excel File with Declines saved as {self.ga_name}_declines.xlsx", "-")

        raise SystemExit

    def display_row_ui(self, index, row):
        row_list = []
        for col_name in self.col:
            row_list.append(row[col_name])

        if self.again:
            pretty_print(f"Index: {index + 1} / Called: {self.called} / Not Answered: {self.not_answered} / Declines: {self.declines}", "/")
            self.simple_function(row)
            self.call_result(row_list)
            self.looping()
            clear()

        if not self.again:
            self.not_called_list.append(row_list)

    def looping(self):
        """ Function to loop again """

        pretty_print("To Exit enter: 101", ":")
        pretty_print("To continue press any number key:", ":")
        decision = get_int_input()

        if decision == 101:
            self.again = False

    def simple_function(self, row):
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

    def call_result(self, row_list):
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
                self.called += 1
                again = False
                self.called_list.append(row_list)

            elif result == 500:
                self.not_answered += 1
                again = False
                self.no_answer_list.append(row_list)

            elif result == 999:
                again = False

            elif result == 404:
                self.declines += 1
                again = False
                self.decline_list.append(row_list)

            else:
                print("You can't get out of this! Enter a valid number!")

    def email_options(self):
        pretty_print("To send Email updates press: 200", "*")
        pretty_print("To continue press any number key:", "*")
        choice = get_int_input()

        if choice == 200:

            try:
                main_email(self.ga_name, self.total, self.called, self.not_answered, self.declines, self.not_called)
            except Exception as log_error:
                pretty_print("Server error...Couldn't send the email updates", ":")
                print(log_error)

def ga_assist_main():
    """ Main GA Assist Function """

    clear()
    pretty_print("Hi GAs! Hope you enjoy Calling Campaigns from now", "#")
    ga_name = input("Enter your Name: \n")

    try:
        name = get_file()

    except FileNotFoundError:
        clear()
        pretty_print("The File Does not Exist.", ":")
        pretty_print("Make Sure your place the file in the working directory.", ":")
        sleep(5)
        ga_assist_main()

    else:
        GAassist(ga_name, name)
