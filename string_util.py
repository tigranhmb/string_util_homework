import datetime
content = "One morning, when Gregor Sam5a woke fr0m troubled dream5, he found h1mself transformed in hi5 bed into a h0rr1ble verm1n."


def findNumbers(content):
    return [char for char in content if (char.isdigit()) == True]
print(findNumbers(content))

def checkDate(date):
    isDate = True
    day, month, year = date.split('/')
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isDate = False
    return isDate


def testfunchayk():
    tebabarior = True
    return tebabarior


def count_each_mark(punc_markk):
    print("The number of" + " " + str(punc_markk) + " " + "mark in the file is" + " " + str(content.count(punc_markk)) + ".")
punc_marks=("," "." "?" ";" "-" ":" "!")
#print each markk
for i in range(0, len(punc_marks)):
    count_each_mark(str(punc_marks[i]))