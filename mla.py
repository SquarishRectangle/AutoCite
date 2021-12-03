from tools import *
import nullabledate


#get the author and title since it's the same for almost all the things
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
            if rawAuthors[0] == "et al":
                authors += "et al"
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
    #create effective title (used for alphabetizing)
    eTitle = ""
    delChars = 0

    for word in title.split():
        if not word.lower() in ("a", "an", "the"):
            eTitle += word + " "

    if noAuthor:
        ILC = eTitle.split()[0]

    return [authors, title, eTitle, ILC]


#get publication since it's the same across many modes
def publication(subjectName, italicize=False):
    name = inp("Enter the " + subjectName)
    if italicize:
        name = '*' + name + '*'
    return name + ", "


#get the database and URL since it's also common across many modes
def databaseURL(italicize=False):
    db = inp("Enter database (enter 'ndb' or 'no database' if database is missing)")
    #return none since there isn't an url either if theres no database
    if db == "ndb" or db == "no database":
        return None

    #properly italisize if required
    if italicize:
        db = '*' + db + "*, "

    #get url
    url = inp("Enter URL") + ". "
    return [db, url]


#journal section
def journal():
    #get the author and title
    aT = authorTitle("article")

    authors = aT[0]
    title = "\"" + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    #get the journal name
    journalName = publication("title of the journal", True)

    #get volume and issue numbers
    volume = "vol. " + inp("Enter volume number") + ', '
    issue = inp("Enter issue number")
    if issue:
        issue = "no. " + issue + ', '

    #get date. This isn't a function since it's subtly different across different modes
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

    #get page numbers
    page = ""
    pg = getPages()
    if pg:
        page = "pp. " + str(pg[0]) + '-' + str(pg[1]) + ". "

    #get database and url
    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + journalName + volume + issue + strDate + page + db + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


#news article
def news():
    #get the author and title
    aT = authorTitle("news article")

    authors = aT[0]
    title = "\"" + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    #get publisher name
    publisher = publication("publisher", True)

    #get date. This isn't a function since it's subtly different across different modes
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

    #get url
    url = inp("Enter URL") + ". "

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + publisher + strDate + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


#physically printed books
def printBook():
    #get author and title
    aT = authorTitle("book")

    authors = aT[0]
    title = '*' + aT[1] + "*. "
    eTitle = aT[2]
    ILC = aT[3]

    #get edition number
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

    #get publisher
    publisher = publication("publisher")

    #get date. This isn't a function since it's subtly different across different modes
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

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + edition + publisher + strDate
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


#eBooks
def eBook():
    #get author and title
    aT = authorTitle("book")

    authors = aT[0]
    title = '*' + aT[1] + "*, "
    eTitle = aT[2]
    ILC = aT[3]

    #get editors
    editors = "edited by " + inp("Enter editor names") + ". "

    #get publisher
    publisher = publication("publisher")

    #get date. This isn't a function since it's subtly different across different modes
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

    #get database and url
    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + editors + publisher + strDate + db + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


#specific chapters in books
def chapter():
    #get author and title of the chapter
    aT = authorTitle("chapter")

    authors = aT[0]
    title = '\"' + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    #get the book name
    book = publication("name of the book", True)

    #get the editors
    editors = "edited by " + inp("Enter editor names") + ", "

    #get the publisher
    publisher = publication("publisher")

    #get date. This isn't a function since it's subtly different across different modes
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

    #get page number
    page = ""
    pg = getPages()
    if pg:
        page = "pp. " + str(pg[0]) + '-' + str(pg[1]) + ". "

    #get database and url
    dburl = databaseURL(True)
    db = ""
    url = ""
    if dburl:
        db = dburl[0]
        url = dburl[1]

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + book + editors + publisher + strDate + page + db + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])


#web pages
def web():
    #get author and title
    aT = authorTitle("chapter")

    authors = aT[0]
    title = '\"' + aT[1] + "\" "
    eTitle = aT[2]
    ILC = aT[3]

    #get publisher
    publisher = publication("publisher", True)

    #get url
    url = inp("Enter URL") + ". "

    #create the citation and file containing the proper citation, effective title and in line citation
    citation = authors + title + publisher + url
    createFile("Citations/MLA", authors[:-2], [eTitle, ILC, citation])