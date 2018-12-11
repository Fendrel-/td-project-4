from entry import Entry


class ByEmployee():
    def __init__(self):
        names = []
        for count, entry in enumerate(Entry.select()):
            if entry.employee_name not in names:
                names.append(entry.employee_name)
        self.names = names


class ByDate():
    def __init__(self):
        datestring = []
        dates = []
        for count, entry in enumerate(Entry.select()):
            date = entry.date.strftime(format='%m/%d/%Y')
            if date not in datestring:
                datestring.append(date)
                dates.append(entry.date)
        self.datestring = datestring
        self.dates = dates

    def Display(self):
        print(self.datestring)

    def Delete():
        pass

    def Edit():
        pass


class ByTerm():
    pass
