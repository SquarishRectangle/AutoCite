import re

class Date:
    def __init__(self, year, month, day, nodate=False):
        self.year = year
        self.day = day
        self.month = month
        self.nodate = nodate

        if month == 1:
            self.strMonth = "Jan."
        elif month == 2:
            self.strMonth = "Feb."
        elif month == 3:
            self.strMonth = "Mar."
        elif month == 4:
            self.strMonth = "Apr."
        elif month == 5:
            self.strMonth = "May"
        elif month == 6:
            self.strMonth = "June"
        elif month == 7:
            self.strMonth = "July"
        elif month == 8:
            self.strMonth = "Aug."
        elif month == 9:
            self.strMonth = "Sep."
        elif month == 10:
            self.strMonth = "Oct."
        elif month == 11:
            self.strMonth = "Nov."
        elif month == 12:
            self.strMonth = "Dec."
        elif not month:
            pass
        else:
            raise Exception("Month out of range")


months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "Apr": 4,
    "May": 5,
    "June": 6,
    "Jun": 6,
    "July": 7,
    "Jul": 7,
    "August": 8,
    "September": 9,
    "Spt": 9,
    "Sept": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

abrvmonths = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def parser(string):
    if string == "nd" or string == "no date":
        return Date(None, None, None, True)

    string = string.lower()
    monthkeylist = list(months.keys())
    abrvmonthkeylist = list(abrvmonths.keys())

    for i in range(len(monthkeylist)):
        monthkeylist[i] = monthkeylist[i].lower()
    for i in range(len(abrvmonthkeylist)):
        abrvmonthkeylist[i] = abrvmonthkeylist[i].lower()

    #scanning for year
    year = None
    month = None
    day = None

    for i in range(len(string) - 3):
        if string[i:i + 4].isnumeric():
            year = int(string[i:i + 4])
            string = string[:i] + string[i + 4:]
            break

    #scan for month in string
    strMonth = False
    for i in range(9, 2, -1):
        if len(string) >= i:
            for j in range(len(string) - i):
                if string[j:j + i] in monthkeylist:
                    month = list(months.values())[monthkeylist.index(string[j:j + i])]
                    strMonth = True
                    break

                if string[j:j + i] in abrvmonthkeylist:
                    month = list(abrvmonths.values())[abrvmonthkeylist.index(string[j:j + i])]
                    strMonth = True
                    break
            else:
                continue
            break

    if not strMonth:
        liststr = re.split(" |/|\\|,", string)
        for s in liststr:
            if len(s) == 1:
                try:
                    if int(s) < 13:
                        month = int(s)
                        strMonth = True
                        break
                except:
                    pass

    #scanning for month and day
    doublepairs = []
    for i in range(len(string) - 1):
        if string[i:i + 2].isnumeric():
            doublepairs.append(int(string[i:i + 2]))
            string = string[:i] + string[i + 2:]

    #determining month vs day
    if not strMonth:
        if len(doublepairs) == 1:
            month = doublepairs[0]
        elif len(doublepairs) == 2:
            if doublepairs[0] < 13:
                month = doublepairs[0]
                day = doublepairs[1]
            elif doublepairs[1] < 13:
                month = doublepairs[1]
                day = doublepairs[0]
    else:
        if len(doublepairs) == 1:
            day = doublepairs[0]

    return Date(year, month, day)