from entry import Entry


class ByEmployee():
    pass


class ByDate():
    def __init__(self):
        dates = []
        for count, entry in enumerate(Entry.select()):
            dates.append(entry.date.strftime(format='%m/%d/%Y'))
        self.dates = dates


class ByTimeSpent():
    pass


class ByTerm():
    pass
