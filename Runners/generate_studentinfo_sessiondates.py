"""
Description: initial generate caller to get students-session dates into .txt
"""
from pprint import pprint, pformat
from StudentManager.student_info import StudentInfo
from Runners.studentinfo_date_store import StudentInfoDateStore


class GenerateStudentSessionDates(object):
    def __init__(self):
        self.studentDataStoreDict = {}

    def getMonthValueInput(self):
        isValidMonthCheck = False
        while not isValidMonthCheck:
            month = raw_input("\n enter a numerical month : \n")
            monthVal, monthIsNumber = self.validateNumericalInput(month)
            if monthIsNumber and self.isValidMonth(monthVal):
                isValidMonthCheck = True
            else:
                print "**ERROR**: %s isn't a valid month - valid month from 1 to 12" % monthVal
        return monthVal

    def getYearValueInput(self):
        yearIsNumberCheck = False
        while not yearIsNumberCheck:
            year = raw_input("\n enter a numerical year : \n")
            yearVal, yearIsNumberCheck = self.validateNumericalInput(year)
            if not yearIsNumberCheck:
                print "**ERROR**: %s isn't a valid year" % yearVal
        return yearVal

    def getStudentNameInput(self):
        studentName = raw_input("\n enter student name(s): eg - Evelyn \t Benjamin;Zeming \t Tim;Mel;Wes \n")
        return studentName

    def getSelectDaysInput(self):
        validWeekdaysMsg = "Valid weekdays are: M T W TH F \n"
        validSelectDays = False
        while not validSelectDays:
            selectDays = raw_input("\n enter session weekdays: eg - M \t W,TH \t T,W,TH \t T,TH,F \n")
            validSelectDays = self.validateWeekdayInput(selectDays)
            if not validSelectDays:
                print validWeekdaysMsg
        return selectDays

    def validateNumericalInput(self, inputValue):
        isNumerical = True
        try:
            inputValue = int(self, inputValue)
        except ValueError:
            print "**ERROR**: %s entry isn't numerical" % inputValue
            isNumerical = False
        return inputValue, isNumerical

    def isValidMonth(self, inputMonth):
        return inputMonth in range(1,13)

    def validateWeekdayInput(self, inputValue):
        inputValueSet = set(inputValue.split(","))
        validWeekdaysSet = set(["M", "T", "W", "TH", "F"])
        return len(inputValueSet.intersection(validWeekdaysSet)) == len(inputValueSet)

    def runToGetStudentInfoAndSessionDates(self):
        print "\n this script will save the student(s) name & session dates for the same month, year \n"
        studentsList = []

        monthVal = self.getMonthValueInput()
        yearVal = self.getYearValueInput()
        print "\n will be getting dates for month %d, year %d \n" % (monthVal, yearVal)

        quitLoop = False
        while not quitLoop:
            studentName = self.getStudentNameInput()
            selectDays = self.getSelectDaysInput()
            print "\n will be getting %s days for %s \n" % (selectDays, studentName)

            studentObj = StudentInfo(studentName, monthVal, yearVal, selectDays)
            studentsList.append(studentObj.getStudentNameAndSessionDaysAndDates())
            for s in studentsList:
                print "\n student(s) : %s, total session dates retrieved: %d \n" % (s[0], len(s[1]))
            # print studentsList

        self.studentDataStoreDict = StudentInfoDateStore(studentsList).getStudentsDict()


if __name__ == "__main__":
    GenerateStudentSessionDates().runToGetStudentInfoAndSessionDates()
    print "end program"