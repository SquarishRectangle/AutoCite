import os
import copy
import nullabledate

#just some of my standard functions that i use everywhere
def clone(var):
    return copy.deepcopy(var)

#just some of my standard functions that i use everywhere
def inp(msg, lower=False):
    usr = ''
    print (msg)
    while True:
        txt = input()
        if txt == '':
            break
        usr += txt + ' '

    if usr:
        while usr[-1] == ' ':
            usr = usr[:-1]

    if lower:
        usr = usr.lower()

    return usr

#create and write to a file
def createFile(path, filename, contents=None):
    #create directory if not exists
    while not os.path.exists(path):
        os.makedirs(path)

    #add the path together
    fPath = path + '/' + filename

    #create the file. (if it already exists append an integer to the end of file name)
    i = 2
    if os.path.exists(fPath):
        fPath += str(i)
        while os.path.exists(fPath):
            i += 1
            fPath = path + filename + str(i)

    file = open(fPath + ".txt", 'a')
    #write to file if needed
    if contents:
        for c in contents:
            file.write(c + "\n\n")
    file.close()
    print ("Your citation has been generated to " + fPath + ".txt")


#get author function (it lives here because I originally wanted to do APA as well as MLA but i ran out of time)
def getAuthors(cFormat):
    authors = []
    #if the format is mla which it always is :/
    if cFormat == "mla":
        #while loop to make sure a correct input is returned
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

#get date function returns a nullabledate.Date data type
def getDate():
    usrDate = inp("Enter date (enter 'nd' or 'no date' if date is missing)")
    return nullabledate.parser(usrDate)

#get pages. returns a list of starting and ending page
def getPages():
    #get starting page
    while True:
        pgs = inp("Enter start page (enter 'np' or 'no page' if page numbers are missing)")
        if pgs == "np" or pgs == "no page":
            return None

        try:
            pgs = int(pgs)
            break
        except:
            print ("Enter a valid number")

    #get ending page
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