import os
import copy
import nullabledate

def clone(var):
    return copy.deepcopy(var)

def inp(msg, lower=False):
    usr = input(msg + "\n$ ")
    if usr:
        while usr[-1] == ' ':
            usr = usr[:-1]
    if lower:
        usr = usr.lower()
    return usr

def createFile(path, filename, contents=None):
    while not os.path.exists(path):
        os.makedirs(path)

    fPath = path + '/' + filename

    i = 2

    if os.path.exists(fPath):
        fPath += str(i)
        while os.path.exists(fPath):
            i += 1
            fPath = path + filename + str(i)

    file = open(fPath + ".txt", 'a')
    if contents:
        for c in contents:
            file.write(c + "\n\n")
    file.close()
    print ("Your citation has been generated to " + fPath + ".txt")


def getAuthors(cFormat):
    authors = []
    if cFormat == "mla":
        while True:
            numAuthors = inp("How many authors are there? ")
            try:
                numAuthors = int(numAuthors)
            except Exception:
                numAuthors = -1

            if numAuthors == 0:
                authors.append('')
                return authors
            elif numAuthors == 1:
                a = inp("Enter author name")
                authors.append(a)
                return authors
            elif numAuthors == 2:
                a = inp("Enter primary author name")
                authors.append(a)
                a = inp("Enter secondary author name")
                authors.append(a)
                return authors
            elif numAuthors > 2:
                a = inp ("Enter primary author name")
                authors.append(a)
                authors.append("et al")
                return authors
            else:
                print ("Please enter a valid number of authors")

def getDate():
    usrDate = inp("Enter date (enter 'nd' or 'no date' if date is missing)")
    return nullabledate.parser(usrDate)

def getPages():
    while True:
        pgs = inp("Enter start page (enter 'np' or 'no page' if page numbers are missing)")
        if pgs == "np" or pgs == "no page":
            return None

        try:
            pgs = int(pgs)
            break
        except:
            print ("Enter a valid number")

    while True:
        pge = inp("Enter end page (enter 'np' or 'no page' if page numbers are missing)")
        if pge == "np" or pge == "no page":
            return None

        try:
            pge = int(pge)
            break
        except:
            print ("Enter a valid number")

    return [pgs, pge]