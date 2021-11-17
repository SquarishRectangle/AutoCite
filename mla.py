from tools import *
import nullabledate

def authorTitle(subjectName):
    noAuthor = False
    #rawAuthors
    rawAuthors = getAuthors("mla")
    if rawAuthors[0]:
        #first author
        rawAuthors[0] = rawAuthors[0].split()
        #lastname
        lastname = rawAuthors[0][-1]
        authors = lastname + ", "
        del rawAuthors[0][-1]
        #first and middle names
        for name in rawAuthors[0]:
            authors += name + ' '
        del rawAuthors[0]

        #other authors
        if rawAuthors:
            if rawAuthors[0] == "et al.":
                authors += "et al. "
                ILC = "(" + lastname + " et al.)"
            else:
                authors += "and " + rawAuthors[0]
                ILC = "(" + lastname + ", and " + rawAuthors[0].split()[-1] + ")"
        else:
            ILC = "(" + lastname + ")"
            authors = authors[:-1]

        authors += ". "
    else:
        noAuthor = True
        authors = ""


    #title

    title = inp("Enter the title of the " + subjectName)
    #create effective title
    eTitle = ""
    delChars = 0

    for word in title.split():
        if not word.lower() in ("a", "an", "the"):
            eTitle += word + " "

    if noAuthor:
        ILC = eTitle.split()[0]

    return [authors, title, eTitle, ILC]


def publication(subjectName, italicize=False):
    name = inp("Enter the " + subjectName)
    if italicize:
        name = '*' + name + '*'
    return name + ", "


def databaseURL(italicize=False):
    db = inp("Enter database (enter 'ndb' or 'no database' if database is missing)")
    if db == "ndb" or db == "no database":
        return None

    if italicize:
        db = '*' + db + "*, "

    url = inp("Enter URL") + ". "
    return [db, url]


def journal():
    aT = authorTitle("article")

    authors = aT[0]
    title = "\"" + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    journalName = publication("title of the journal", True)

    volume = "vol. " + inp("Enter volume number") + ', '
    issue = inp("Enter issue number")
    if issue:
        issue = "no. " + issue + ', '

    while True:
        date = getDate()
        if date.year or date.nodate:
            break
        else:
            print ("Missing year")

    strDate = ""
    if not date.nodate:
        if date.year:
            strDate = str(date.year) + ', '
            if date.month:
                strDate = date.strMonth + ' ' + strDate
                if date.day:
                    strDate = str(date.day) + ' ' + strDate

    page = ""

    pg = getPages()

    if pg:
        page = "pp. " + str(pg[0]) + '-' + str(pg[1]) + ". "

    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    citation = authors + title + journalName + volume + issue + strDate + page + db + url

    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


def news():
    aT = authorTitle("news article")

    authors = aT[0]
    title = "\"" + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    publisher = publication("publisher", True)

    while True:
        date = getDate()
        if date.year or date.nodate:
            break
        else:
            print ("Missing year")

    strDate = ""
    if not date.nodate:
        if date.year:
            strDate = str(date.year) + ', '
            if date.month:
                strDate = date.strMonth + ' ' + strDate
                if date.day:
                    strDate = str(date.day) + ' ' + strDate

    url = inp("Enter URL") + ". "

    citation = authors + title + publisher + strDate + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


def printBook():
    aT = authorTitle("book")

    authors = aT[0]
    title = '*' + aT[1] + "*. "
    eTitle = aT[2]
    ILC = aT[3]

    edition = ""
    while True:
        edition = inp("Enter edition number (if there are any)")
        if not edition:
            break
        try:
            edition = int(edition)
            if edition == 1:
                edition = "1st"
                break
            elif edition == 2:
                edition = "2nd"
                break
            else:
                edition = str(edition) + "th"
                break
        except:
            print ("Please enter a valid number")

    if edition:
        edition += " ed., "

    publisher = publication("publisher")

    while True:
        date = getDate()
        if date.year or date.nodate:
            break
        else:
            print ("Missing year")

    strDate = ""
    if not date.nodate:
        if date.year:
            strDate = str(date.year) + '. '
            if date.month:
                strDate = date.strMonth + ' ' + strDate
                if date.day:
                    strDate = str(date.day) + ' ' + strDate

    citation = authors + title + edition + publisher + strDate
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


def eBook():
    aT = authorTitle("book")

    authors = aT[0]
    title = '*' + aT[1] + "*, "
    eTitle = aT[2]
    ILC = aT[3]

    editors = "edited by " + inp("Enter editor names") + ". "

    publisher = publication("publisher")

    while True:
        date = getDate()
        if date.year or date.nodate:
            break
        else:
            print ("Missing year")

    strDate = ""
    if not date.nodate:
        if date.year:
            strDate = str(date.year) + '. '
            if date.month:
                strDate = date.strMonth + ' ' + strDate
                if date.day:
                    strDate = str(date.day) + ' ' + strDate

    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    citation = authors + title + editors + publisher + strDate + db + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


def chapter():
    aT = authorTitle("chapter")

    authors = aT[0]
    title = '\"' + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    book = publication("name of the book", True)

    editors = "edited by " + inp("Enter editor names") + ", "

    publisher = publication("publisher")

    while True:
        date = getDate()
        if date.year or date.nodate:
            break
        else:
            print ("Missing year")

    strDate = ""
    if not date.nodate:
        if date.year:
            strDate = str(date.year) + '. '
            if date.month:
                strDate = date.strMonth + ' ' + strDate
                if date.day:
                    strDate = str(date.day) + ' ' + strDate

    page = ""

    pg = getPages()

    if pg:
        page = "pp. " + str(pg[0]) + '-' + str(pg[1]) + ". "

    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    citation = authors + title + book + editors + publisher + strDate + page + db + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


def web():
    aT = authorTitle("chapter")

    authors = aT[0]
    title = '\"' + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    publisher = publication("publisher", True)

    url = inp("Enter URL") + ". "

    citation = authors + title + publisher + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])