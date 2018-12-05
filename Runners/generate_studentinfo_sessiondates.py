"""
Description: initial generate caller to get students-session dates into .txt
"""

from StudentManager.student_info import StudentInfo
from Runners.studentinfo_date_store import StudentInfoDateStore

def validateNumericalInput(inputValue):
    isNumerical = True
    try:
        inputValue = int(inputValue)
    except ValueError:
        print "**ERROR**: %s entry isn't numerical" % inputValue
        isNumerical = False
    return inputValue, isNumerical

def isValidMonth(inputMonth):
    return inputMonth in range(1,13)

def validateWeekdayInput(inputValue):
    inputValueSet = set(inputValue.split(","))
    validWeekdaysSet = set(["M", "T", "W", "TH", "F"])
    return len(inputValueSet.intersection(validWeekdaysSet)) == len(inputValueSet)


def runToGetStudentInfoAndSessionDates():
    print "\n this script will save the student(s) name & session dates for the same month, year \n"
    studentsList = []

    # enter the loop here
    isValidMonthCheck = False
    while not isValidMonthCheck:
        month = raw_input("\n enter a numerical month : \n")
        monthVal, monthIsNumber = validateNumericalInput(month)
        if monthIsNumber and isValidMonth(monthVal):
            isValidMonthCheck = True
        else:
            print "**ERROR**: %s isn't a valid month - valid month from 1 to 12" % monthVal

    yearIsNumberCheck = False
    while not yearIsNumberCheck:
        year = raw_input("\n enter a numerical year : \n")
        yearVal, yearIsNumberCheck = validateNumericalInput(year)
        if not yearIsNumberCheck:
            print "**ERROR**: %s isn't a valid year" % yearVal

    print "\n will be getting dates for month %d, year %d \n" % (monthVal, yearVal)

    studentName = raw_input("\n enter student name(s): eg - Evelyn \t Benjamin;Zeming \t Tim;Mel;Wes \n")

    validWeekdaysMsg = "Valid weekdays are: M T W TH F"
    validSelectDays = False
    while not validSelectDays:
        selectDays = raw_input("enter session weekdays: eg - M \t W,TH \t T,W,TH \t T,TH,F \n")
        validSelectDays = validateWeekdayInput(selectDays)
        if not validSelectDays:
            print validWeekdaysMsg

    print "\n will be getting %s days for %s \n" % (selectDays, studentName)
    studentObj = StudentInfo(studentName, monthVal, yearVal, selectDays)
    studentsList.append(studentObj.getStudentNameAndSessionDaysAndDates())

    for s in studentsList:
        print "\n student(s) : %s, total session dates retrieved: %d \n" % (s[0], len(s[1]))
    # print studentsList


if __name__ == "__main__":
    runToGetStudentInfoAndSessionDates()
    print "end program"