from Entry import db, Entry
from Menu import Menu


def main_menu():
    menu_options = ['Add Entry', 'Search Entries']
    while True:
        Menu.Header("Main Menu")
        Menu.StatusMessage()
        Menu.Options(menu_options, is_Main=True)
        input()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Entry], safe=True)
    main_menu()
