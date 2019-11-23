""" Email Updates Module """

import datetime
from string import Template
import smtplib
import os
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from prettytable import PrettyTable

ADDRESS = "dev.msalvi@gmail.com"
PASSWORD = "Aparna9664443222!"
HOST = "smtp.gmail.com"
PORT = 587

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

def simple_contacts(filename):
    """ Function to get contacts """

    try:
        file_path = open(filename, 'r', encoding='utf-8')

    except FileNotFoundError:
        pretty_print("Cannot open contacts.txt", ":")
        sleep(3)

    else:
        with file_path:
            print_list = []
            email_dict = {}
            for line in file_path:
                split_line = line.strip().split('|')

                if split_line[0].isnumeric():

                    command = int(split_line[0])
                    email = split_line[-1]
                    print_list.append(split_line)
                    email_dict[command] = email

    return print_list, email_dict

def get_emails(print_list, email_dict):
    """ Function to get emails """

    email_list = []
    again = True
    contact_table = PrettyTable()
    contact_table.field_names = ["Command", "Advisor Name", "Email"]

    for row in print_list:
        contact_table.add_row(row)

    while again:
        print(contact_table)
        pretty_print(email_list, ":")
        pretty_print("To Add Receiving Emails Enter the corresponding command number", "-")
        pretty_print("To Send Mail press any number key:", "-")
        choice = get_int_input()
        if choice in email_dict.keys():
            email_list.append(email_dict[choice])

        else:
            if len(email_list) != 0:
                again = False

            else:
                again = True
                pretty_print("No Email Added", "-")

        clear()

    return email_list

def read_template():
    """ Function to get Template String """

    text_msg = """${PERSON_NAME} - Calling Campaign Summary - ${DATE}:\n
                Total Called = ${TOTAL_CALLED}\n
                Answered = ${ANSWERED}\n
                Not Answered = ${NOT_ANSWERED}\n
                Declines = ${DECLINES}\n
                Remaining = ${REMAINING}\n
                \n
                Thank You."""

    return Template(text_msg)

def main_email(name, total, answered, not_answered, declines, remaining):
    """ Main function for sending Email Updates """

    start = smtplib.SMTP(host=HOST, port=PORT)
    start.starttls()
    start.login(ADDRESS, PASSWORD)

    date = datetime.datetime.now()
    date_now = date.strftime("%m-%d-%Y")

    print_list, email_dict = simple_contacts('contacts.txt')

    emails = get_emails(print_list, email_dict)

    message_template = read_template()

    for mail in emails:
        pretty_print(f"Sending email to {mail}", "!")
        msg = MIMEMultipart()

        message = message_template.substitute(PERSON_NAME=name, DATE=date_now, TOTAL_CALLED=total, ANSWERED=answered, NOT_ANSWERED=not_answered, DECLINES=declines, REMAINING=remaining)

        msg['From'] = ADDRESS
        msg['To'] = mail
        msg['Subject'] = f"{name} - Calling Campaign Summary - {date_now}"

        msg.attach(MIMEText(message, 'plain'))
        start.send_message(msg)
        pretty_print(f"Mail sent to {mail}", "!")

        del msg

    start.quit()
