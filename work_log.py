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


def display_entry(query_results, index=0):
    while True:
        current_entry = query_results[index]
        status_message = "\n Displaying entry {} of {}".format(
            index+1, len(query_results))
        menu.Header('Display Entry')
        print('\n Date:      {}'.format(
            current_entry.date.strftime(format='%m/%d/%Y')))
        print(' Employee:  {}'.format(current_entry.employee_name))
        print(' Task:      {}'.format(current_entry.task_name))
        print(' Minutes:   {}'.format(current_entry.time_spent))
        print(' Notes:     {}'.format(current_entry.notes))
        print()
        print('-' * 35)
        menu.StatusMessage(status_message)
        menu_options = ['Previous', 'Next',
                        'Edit', 'Delete']
        menu.Options(menu_options)
        user_choice = user_prompt()
        if user_choice == "1":
            index -= 1
            if index < 0:
                index = len(query_results) - 1
            continue

        elif user_choice == "2":
            index += 1
            if index > len(query_results) - 1:
                index = 0
            continue

        elif user_choice == "4":
            if "Y" in input(' Are you sure you want to delete?: ').upper():
                current_entry.delete()
                if index > len(query_results) - 1:
                    index = index - 1
                current_entry = query_results[index]
            continue

        elif user_choice == "5":
            break
        elif user_choice == "6":
            kill_script()


def search_by_date():
    status_message = None
    menu_options = search.ByDate().datestring
    while True:
        menu.Header('Search By Date')
        menu.StatusMessage(status_message)
        status_message = None
        menu.Options(menu_options)
        user_choice = user_prompt()
        if int(user_choice) == len(menu_options) + 1:
            break
        elif int(user_choice) == len(menu_options) + 2:
            kill_script()
        else:
            display_entry(Entry.select().where(Entry.date == datetime.strptime(
                menu_options[int(user_choice)-1], '%m/%d/%Y')))


def search_entry():

    menu_options = ['Search By Date', 'Search By Employee',
                    'Search By Time Spent', 'Search By Term']
    status_message = None
    while True:
        menu.Header('Search Entries')
        menu.StatusMessage(status_message)
        status_message = None
        menu.Options(menu_options)
        user_choice = user_prompt()
        if user_choice == "1":
            search_by_date()
            continue
        if user_choice == "5":
            break
        elif user_choice == "6":
            kill_script()


def main_menu():
    menu_options = ['Add Entry', 'Search Entries']
    status_message = None
    while True:
        menu.Header('Main Menu')
        menu.StatusMessage(status_message)
        status_message = None
        menu.Options(menu_options, is_Main=True)
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
