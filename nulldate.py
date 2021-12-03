import re

#date data type
class Date:
    #initiate variables since each date is its own variable
    def __init__(self, year, month, day, nodate=False):
        self.year = year
        self.day = day
        self.month = month
        self.nodate = nodate

        #convert to an abbrieveated string month
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
        #pass if month is null
        elif not month:
            pass
        else:
            raise Exception("Month out of range")


#string month dictionary and unusual month abbrieviations
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

#standard month abbrieviations
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

#user input parser
def parser(string):

    if "nd" in string or "no date" in string:
        return Date(None, None, None, True)

    liststr = re.split(" |/|\\\\|,|\.", string)
    year = None
    month = None
    day = None

    for item in liststr:
        if item in months.keys():
            month = months[item]
            del item
            break
        if item in abrvmonths.keys():
            month = abrvmonths[item]
            del item
            break

    ints = []
    for item in liststr:
        if item.isnumeric():
            ints.append(int(item))

    for i in ints:
        if len(str(i)) == 4:
            year = i
            del i
            break

    for i in ints:
        if not month and i <= 12:
            month = i
        elif not day and i <= 31:
            day = i
        elif not year:
            year = i + 2000

    return Date(year, month, day)