""" Data Models for International and Domestic Data """

import datetime
import os
import pandas as pd

class International:
    """ Class for International Student Data Excel Files """

    columns = {
        'enrollInfo': 'App - Enroll Info - Degree of Interest (app)',
        'enrollStatus': 'App - Enroll Info - Enroll Status (app)',
        'bin': 'Bin',
        'citizenship': 'Citizenship1',
        'decision': 'Decision #1 Name',
        'school': 'School Applied for',
        'defer': 'Defer to Term',
        'reporting': 'Reporting Classification',
        'onCampus': 'How do you plan to complete your Stevens degree?',
        'i20Process': 'App - ISSS Info - I-20 Processed Date (Format: day/month/year)',
        'i20Transfer': 'App - ISSS Info - I-20 Transfer',
        'fellowship': 'Fellowship Type',
        'deposit': 'Deposit Received Amount',
        'coa': 'COA Submission Status',
        'lastContact': 'Last Contact Date (Format: month/day/year)'
    }

    def __init__(self, name):
        """ Initialise International Object - Create Pandas Dataframe """

        os.chdir(os.getcwd())
        self.stack = []
        self.name = name
        self.today = datetime.datetime.now()

        try:
            self.data_frame = pd.read_excel(self.name)

        except FileNotFoundError:
            print("Error: File Does not Exist...")

    def enrollment_options(self, choice):
        """ Method to filter through enrollment options """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollInfo']]
                                    .str.contains('Master|Graduate Certificate|Engineer*', regex=True)]

            self.stack.append("Masters/Graduate Certificate")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollInfo']]
                                    .str.contains('^Ph.D.', regex=True)]

            self.stack.append("PhD")

    def enrollment_info(self, choice):
        """ Method to filter through enrollment information """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollStatus']] == "Full-time"]
            self.stack.append("Full-Time")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollStatus']] == "Part-time"]
            self.stack.append("Part-Time")

    def admitted_info(self, choice):
        """ Method to filter through admitted information """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['bin']]
                                              .str.contains('Admit|Conditional Admit', regex=True)]
            
            self.stack.append("Admits/Conditional Admits")

    def citizenship_info(self, choice):
        """ Method to filter through citizenship information """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['citizenship']]
                                    .str.contains('China|South Korea|Vietnam|Taiwan', regex=True) == False]

            self.stack.append("Non-China")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['citizenship']]
                                        .str.contains('China|South Korea|Vietnam|Taiwan', regex=True)]

            self.stack.append("China")

    def declines_info(self, choice):
        """ Method to Remove Declines """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['decision']]
                                            .str.contains('Admit/Decline') == False]

            self.stack.append("Declines Removed")

    def school_info(self, choice):
        """ Method to Filter through Schools """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['school']]
                                              .str.contains('SOB')]

            self.stack.append("School Of Business")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['school']]
                                              .str.contains('SES')]
            
            self.stack.append("School of Engineering and Sciences")

        if choice == 3:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['school']]
                                              .str.contains('SSE')]

            self.stack.append("School of Systems and Enterprises")

    def deferral_info(self, string):
        """ Method to filter through deferrals """

        data_frame1 = self.data_frame[self.data_frame[International.columns['defer']]
                                    .isnull()]

        data_frame2 = self.data_frame.loc[self.data_frame[International.columns['defer']]
                                        .str.contains(string, na=False)]

        frames = [data_frame1, data_frame2]
        self.data_frame = pd.concat(frames)
        self.stack.append(f"Deferred to {string}")

    def reporting_info(self, choice):
        """ Method to filter through Reporting Classification """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['reporting']]
                                        .str.contains('Int', na=False)]

            self.stack.append("Reporting Classification - International")

    def on_campus_info(self, choice):
        """ Method to filter through On Campus Student Data """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['onCampus']]
                                              .str.contains('On-campus classes on the Stevens campus', na=False)]

            self.stack.append("On Campus Students")

    def transfer_info(self, choice):
        """ Method to filter through transferred students """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['i20Transfer']]
                                    .isnull()]
            
            self.stack.append("No Transfers")

    def fellowship_info(self, choice):
        """ Method to filter through fellowship data """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['fellowship']]
                                    .isnull()]

            self.stack.append("No Fellowships")

    def deposit_info(self, choice):
        """ Method to filter through enrollment deposit information """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['deposit']]
                                    .isnull()]

            self.stack.append("Not Paid Deposit")

        if choice == 2:
            self.data_frame = self.data_frame[self.data_frame[International.columns['deposit']]
                                    .notnull()]

            self.stack.append("Paid Deposit")

    def coa_info(self, choice):
        """ Method to filter through Confirmation of Arrival details """

        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['coa']]
                                    .isnull()]

            self.stack.append("Not Submitted COA")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[International.columns['coa']]
                                        .str.contains('Yes - Attending Stevens', na=False)]

            self.stack.append("Submitted COA")

    def i20_info(self, choice):
        """ Method to filter through I20 information """

        i20_issued = False
        if choice == 1:
            self.data_frame = self.data_frame[self.data_frame[International.columns['i20Process']]
                                    .isnull()]

            self.stack.append("No I-20")

        if choice == 2:
            self.data_frame = self.data_frame[self.data_frame[International.columns['i20Process']]
                                    .notnull()]

            self.stack.append("I-20 Issued")
            i20_issued = True

        return i20_issued


    def no_last_contact(self):
        """ Get data with no last contact date """

        self.data_frame = self.data_frame[self.data_frame[International.columns['lastContact']]
                                          .isnull()]
        
        self.stack.append("No Last Contact Date")

    def compare_date_before(self, date):
        """ Get data with last contact date before specified date """

        self.data_frame[International.columns['lastContact']] = pd.to_datetime(self.data_frame[International.columns['lastContact']])
        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['lastContact']] <= date]

    def compare_date_after(self, date):
        """ Get data with last contact date after specified data """

        self.data_frame[International.columns['lastContact']] = pd.to_datetime(self.data_frame[International.columns['lastContact']])
        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['lastContact']] >= date]

    def save(self, string):
        """ Save As Excel File """

        self.data_frame.to_excel(f'{string}_{self.today.strftime("%m-%d-%Y")}.xlsx', index=False)


class Domestic:
    """ Class for Domestic Student Data Excel Files """

    columns = {
        'enrollInfo': 'App - Enroll Info - Degree of Interest (app)',
        'enrollStatus': 'Enroll Status (app)',
        'lastContact': 'App - Enroll Info - Last Contact Date (Format: month/day/year)'
    }

    def __init__(self, name):
        """ Initialise Domestic Object - Create Pandas Dataframe"""

        os.chdir(os.getcwd())
        self.stack = []
        self.name = name
        self.today = datetime.datetime.now()

        try:
            self.data_frame = pd.read_excel(self.name)

        except FileNotFoundError:
            print("Error: File Does not Exist...")

    def enrollment_options(self, choice):
        """ Method to filter through Graduate and PhD applications """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollInfo']]
                                        .str.contains('Master|Graduate Certificate|Engineer*', regex=True)]

            self.stack.append("Masters/Graduate Certificate")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollInfo']]
                                        .str.contains('^Ph.D.', regex=True)]

            self.stack.append("PhD")

    def enrollment_info(self, choice):
        """ Method to filter through Enrollment status """

        if choice == 1:
            self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollStatus']] == "Full-time"]
            self.stack.append("Full-Time")

        if choice == 2:
            self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollStatus']] == "Part-time"]
            self.stack.append("Part-Time")

    def no_last_contact(self):
        """ Get data with no last contact date """

        self.data_frame = self.data_frame[self.data_frame[Domestic.columns['lastContact']]
                                          .isnull()]

        self.stack.append("No last contact date")

    def compare_date_before(self, date):
        """ Get data with last contact date before specified date """

        self.data_frame[Domestic.columns['lastContact']] = pd.to_datetime(self.data_frame[Domestic.columns['lastContact']])
        self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['lastContact']] <= date]

    def compare_date_after(self, date):
        """ Get data with last contact date after specified date """

        self.data_frame['App - Enroll Info - Last Contact Date (Format: month/day/year)'] = pd.to_datetime(self.data_frame['App - Enroll Info - Last Contact Date (Format: month/day/year)'])
        self.data_frame = self.data_frame.loc[self.data_frame['App - Enroll Info - Last Contact Date (Format: month/day/year)'] >= date]

    def save(self, string):
        """ Save As Excel File """

        self.data_frame.to_excel(f'{string}_{self.today.strftime("%m-%d-%Y")}.xlsx', index=False)
