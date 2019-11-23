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
        self.name = name
        self.today = datetime.datetime.now()

        try:
            self.data_frame = pd.read_excel(self.name)

        except FileNotFoundError:
            print("Error: File Does not Exist...")

    def master(self):
        """ Get Masters/Graduate Certificate Data """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollInfo']]
                                              .str.contains('Master|Graduate Certificate|Engineer*', regex=True)]

    def doctoral(self):
        """ Get Doctoral Data """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollInfo']]
                                              .str.contains('^Ph.D.', regex=True)]

    def full_time_international(self):
        """ Get Full Time Student Data """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollStatus']] == "Full-time"]

    def part_time_international(self):
        """ Get Part Time Student Data """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['enrollStatus']] == "Part-time"]

    def admitted_bin(self):
        """ Get Admits/Conditional Admits """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['bin']]
                                              .str.contains('Admit|Conditional Admit', regex=True)]

    def citizenship_china(self):
        """ Get Data with Chinese Citizenship """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['citizenship']]
                                              .str.contains('China|South Korea|Vietnam|Taiwan', regex=True)]

    def citizenship_non_china(self):
        """ Get Data with Non Chinese Citizenship """

        self.data_frame = self.data_frame[self.data_frame[International.columns['citizenship']]
                                          .str.contains('China|South Korea|Vietnam|Taiwan', regex=True) == False]

    def no_declines(self):
        """ Remove data with declines """

        self.data_frame = self.data_frame[self.data_frame[International.columns['decision']]
                                          .str.contains('Admit/Decline') == False]

    def school(self, string):
        """ Get data by school """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['school']]
                                              .str.contains(string)]

    def defer(self, string):
        """ Get applications deferred to a specific term """

        data_frame1 = self.data_frame[self.data_frame[International.columns['defer']]
                                      .isnull()]

        data_frame2 = self.data_frame.loc[self.data_frame[International.columns['defer']]
                                          .str.contains(string, na=False)]

        frames = [data_frame1, data_frame2]
        self.data_frame = pd.concat(frames)

    def reporting(self):
        """ Get data by reporting classification """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['reporting']]
                                              .str.contains('Int', na=False)]

    def on_campus(self):
        """ Get On-Campus Student data """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['onCampus']]
                                              .str.contains('On-campus classes on the Stevens campus', na=False)]

    def no_i20(self):
        """ Get data with no I-20 """

        self.data_frame = self.data_frame[self.data_frame[International.columns['i20Process']]
                                          .isnull()]

    def no_transfer(self):
        """ Get data with no transfers """

        self.data_frame = self.data_frame[self.data_frame[International.columns['i20Transfer']]
                                          .isnull()]

    def no_fellowship(self):
        """ Get data with no fellowships """

        self.data_frame = self.data_frame[self.data_frame[International.columns['fellowship']]
                                          .isnull()]

    def no_deposit(self):
        """ Get data with no deposit paid """

        self.data_frame = self.data_frame[self.data_frame[International.columns['deposit']]
                                          .isnull()]

    def no_coa(self):
        """ Get data with no COA """

        self.data_frame = self.data_frame[self.data_frame[International.columns['coa']]
                                          .isnull()]

    def yes_coa(self):
        """ Get data with submitted COA """

        self.data_frame = self.data_frame.loc[self.data_frame[International.columns['coa']]
                                              .str.contains('Yes - Attending Stevens', na=False)]

    def yes_deposit(self):
        """ Get data with paid deposit """

        self.data_frame = self.data_frame[self.data_frame[International.columns['deposit']]
                                          .notnull()]

    def yes_i20(self):
        """ Get data with processed I-20 """

        self.data_frame = self.data_frame[self.data_frame[International.columns['i20Process']]
                                          .notnull()]

    def no_last_contact(self):
        """ Get data with no last contact date """

        self.data_frame = self.data_frame[self.data_frame[International.columns['lastContact']]
                                          .isnull()]

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
        self.name = name
        self.today = datetime.datetime.now()

        try:
            self.data_frame = pd.read_excel(self.name)

        except FileNotFoundError:
            print("Error: File Does not Exist...")

    def master(self):
        """ Get Masters/Graduate Certificate Data """

        self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollInfo']]
                                              .str.contains('Master|Graduate Certificate|Engineer*', regex=True)]

    def doctoral(self):
        """ Get doctoral data """

        self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollInfo']]
                                              .str.contains('^Ph.D.', regex=True)]

    def full_time(self):
        """ Get Full Time Student Data """

        self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollStatus']] == "Full-time"]

    def part_time(self):
        """ Get Part Time Student Data """

        self.data_frame = self.data_frame.loc[self.data_frame[Domestic.columns['enrollStatus']] == "Part-time"]

    def no_last_contact(self):
        """ Get data with no last contact date """

        self.data_frame = self.data_frame[self.data_frame[Domestic.columns['lastContact']]
                                          .isnull()]

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
