from tools import *
import mla

#mode selection
mode = inp('''
Welcome to AutoCite!
What are you citing today?
    1 - Journal Article
    2 - News Article
    3 - Print Book
    4 - eBook
    5 - Book Chapter
    6 - Web Page
''', True)

#actually go to the section of the code
if mode == '1' or mode == "journal article":
    mla.journal()
elif mode == '2' or mode == "news article":
    mla.news()
elif mode == '3' or mode == "print book":
    mla.printBook()
elif mode == '4' or mode == "ebook":
    mla.eBook()
elif mode == '5' or mode == "book chapter":
    mla.chapter()
elif mode == '6' or mode == "web page":
    mla.web()

#ask user to retry if they accidentally hit the wrong key
else:
    print ("Please choose a mode")