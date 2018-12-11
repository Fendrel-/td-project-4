import os


class Header():
    def __init__(self, header):
        os.system('cls')
        print('-' * 35)
        print(' ' * (17 - int(len(header)/2)) + header.upper())
        print('-' * 35)


class StatusMessage():
    def __init__(self, status_message):
        if status_message:
            print('\n' + status_message)


class Options():
    def __init__(self, menu_options, is_Main=False, date_range=False, employee_name=False):
        print('')
        for count, item in enumerate(menu_options, start=1):
            print(' [{}] '.format(count) + item)
        count += 1
        if not is_Main:
            if date_range:
                print('\n [{}] Search By Date Range'.format(count))
                count += 1
            elif employee_name:
                print('\n [{}] Enter Employee Name'.format(count))
                count += 1
            print('\n [{}] Return to Previous Menu'.format(count))
            count += 1
            print(' [{}] Quit'.format(count))
        else:
            print('\n [{}] Quit'.format(count))
