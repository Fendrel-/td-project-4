import os
from datetime import datetime

from entry import Entry, db
import menu
import search


def kill_script():
    os.system('cls')
    quit()


def user_prompt():
    return input('\n Choose an option: ')


def add_entry():
    status_message = None
    while True:
        menu.Header('Add Entry')
        menu.StatusMessage(status_message)
        try:
            Entry.New()
            return " Entry added successfully!"
        except:
            return " Error: Entry could not be added."


def print_menu(header, menu_options=None, status_message=None, is_main=False):
    menu.Header(header)
    menu.StatusMessage(status_message)
    if menu_options:
        menu.Options(menu_options, is_main)


def display_entry(query_results, index=0):
    status_message = None
    while True:
        current_entry = query_results[index]
        menu.Header('Display Entry')
        print('\n Date:      {}'.format(
            current_entry.date.strftime(format='%m/%d/%Y')))
        print(' Employee:  {}'.format(current_entry.employee_name))
        print(' Task:      {}'.format(current_entry.task_name))
        print(' Minutes:   {}'.format(current_entry.time_spent))
        print(' Notes:     {}'.format(current_entry.notes))
        print('\n\n Displaying entry {} of {}'.format(
            index+1, len(query_results)))
        print('\n' + '-' * 35)
        menu.StatusMessage(status_message)
        status_message = None
        menu_options = ['Previous', 'Next',
                        'Edit', 'Delete']
        menu.Options(menu_options)
        user_choice = user_prompt()
        if user_choice == "1":
            index -= 1
            if index < 0:
                index = len(query_results) - 1
            continue
        elif user_choice == "2" or user_choice == "":
            index += 1
            if index > len(query_results) - 1:
                index = 0
            continue
        elif user_choice == "4":
            if "Y" in input(' Are you sure you want to delete?: ').upper():
                current_entry.delete_instance()
                if index > len(query_results) - 1:
                    index = index - 1
                current_entry = query_results[index]
            break
        elif user_choice == "5":
            break
        elif user_choice == "6":
            kill_script()
        else:
            status_message = " Sorry I don't understand that!"


def search_by_date():
    header = "Search By Date"
    while True:
        menu_options = search.ByDate().datestring
        print_menu(header, menu_options)
        user_choice = user_prompt()
        print(len(menu_options))
        if int(user_choice) == len(menu_options) + 1:
            break
        elif int(user_choice) == len(menu_options) + 2:
            kill_script()
        else:
            display_entry(Entry.select().where(Entry.date == datetime.strptime(
                menu_options[int(user_choice)-1], '%m/%d/%Y')))


def search_by_employee():
    header = "Search By Employee"
    while True:
        menu_options = search.ByEmployee().names
        print_menu(header, menu_options)
        user_choice = user_prompt()
        if int(user_choice) == len(menu_options) + 1:
            break
        elif int(user_choice) == len(menu_options) + 2:
            kill_script()
        else:
            display_entry(Entry.select().where(
                Entry.employee_name == menu_options[int(user_choice)-1]))


def search_by_time_spent():
    header = "Search By Employee"
    status_message = None
    while True:
        print_menu(header, status_message)
        user_choice = input('\n Enter a time spent in minutes: ')
        try:
            if int(user_choice) < 1:
                status_message = " You must enter a positive integer!"
                continue
        except ValueError:
            status_message = " Please enter a valid integer!"
            continue
        try:
            display_entry(Entry.select().where(
                Entry.time_spent == int(user_choice)))
        except IndexError:
            return " No matches found!"
        break


def search_by_term():
    header = "Search By Term"
    status_message = None
    while True:
        print_menu(header, status_message)
        user_choice = input('\n Enter a term to search for: ')
        display_entry(Entry.select().where(
            (Entry.employee_name.contains(user_choice)) |
            (Entry.task_name.contains(user_choice)) |
            (Entry.notes.contains(user_choice))))
        break


def search_entry():
    header = "Search Entries"
    menu_options = ['Search By Date', 'Search By Employee',
                    'Search By Time Spent', 'Search By Term']
    status_message = None
    while True:
        print_menu(header, menu_options, status_message)
        user_choice = user_prompt()
        if user_choice == "1":
            status_message = search_by_date()
            continue
        elif user_choice == "2":
            status_message = search_by_employee()
            continue
        elif user_choice == "3":
            status_message = search_by_time_spent()
            continue
        elif user_choice == "4":
            status_message = search_by_term()
            continue
        elif user_choice == "5":
            break
        elif user_choice == "6":
            kill_script()


def main_menu():
    header = "Main Menu"
    menu_options = ['Add Entry', 'Search Entries']
    status_message = None
    while True:
        print_menu(header, menu_options, status_message, is_main=True)
        user_choice = user_prompt()
        if user_choice is "1":
            status_message = add_entry()
            continue
        elif user_choice is "2":
            search_entry()
            continue
        elif user_choice is "3":
            kill_script()
        else:
            status_message = " Sorry I don't understand that!"


if __name__ == "__main__":
    db.connect()
    db.create_tables([Entry], safe=True)
    main_menu()
