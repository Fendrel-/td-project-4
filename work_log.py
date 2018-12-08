import os

import entry
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
            entry.Entry.New()
            return " Entry added successfully!"
        except:
            return " Error: Entry could not be added."


def search_by_date():
    status_message = None
    menu_options = search.ByDate().dates
    while True:
        menu.Header('Search By Date')
        menu.StatusMessage(status_message)
        status_message = None
        menu.Options(menu_options)
        user_choice = user_prompt()


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
    db = entry.db
    db.connect()
    db.create_tables([entry.Entry], safe=True)
    main_menu()
