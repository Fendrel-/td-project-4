class Menu:
    def Header(header):
        print('-' * 35)
        print(' ' * (17 - int(len(header)/2)) + header)
        print('-' * 35)

    def StatusMessage():
        pass

    def Options(menu_options, is_Main=False):
        for count, item in enumerate(menu_options, start=1):
            print(' [{}] '.format(count) + item)
        if not is_Main:
            print('Return to Previous Menu')

    def Prompt():
        pass
