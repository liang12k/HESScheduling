"""
Description: initial generate caller to get students-session dates into .txt
"""
import logging
import datetime
from tabulate import tabulate  # need to pip install
from StudentManager.student_info import StudentInfo
from Runners.studentinfo_date_store import StudentInfoDateStore
from DateManagers.test.test_date_retrieve_constants import EXPECTED_ALL_WEEKDAYS_ABBREV

logging.getLogger().setLevel(logging.WARNING)


class GenerateStudentSessionDates(object):
    def __init__(self):
        self.studentList = []
        self.studentDataStoreDict = {}
        self.month = None
        self.year = None
        self.fileName = "%d_%d_HES_sessions_asOf_%s.txt"
        self.errorMsgPrefix = "*** ERROR *** :"

    def getMonthValueInput(self):
        isValidMonthCheck = False
        while not isValidMonthCheck:
            month = raw_input("\n enter a numerical month : \n")
            monthVal, monthIsNumber = self.validateNumericalInput(month)
            if monthIsNumber and self.isValidMonth(monthVal):
                isValidMonthCheck = True
            else:
                print self.errorMsgPrefix + " %s isn't a valid month - valid month from 1 to 12" % monthVal
        self.month = monthVal
        return monthVal

    def getYearValueInput(self):
        yearIsNumberCheck = False
        while not yearIsNumberCheck:
            year = raw_input("\n enter a numerical year : \n")
            yearVal, yearIsNumberCheck = self.validateNumericalInput(year)
            if not yearIsNumberCheck:
                print self.errorMsgPrefix + " %s isn't a valid year" % yearVal
        self.year = yearVal
        return yearVal

    def getStudentNameInput(self):
        studentNameIsBlank = True
        while studentNameIsBlank:
            studentName = raw_input("\n enter student name(s): eg - Evelyn \t Benjamin;Zeming \t Tim;Mel;Wes \n")
            studentNameIsBlank = studentName.strip() == ""
            if studentNameIsBlank:
                print "** blank name entered, please provide a name **"
        return studentName

    def getSelectDaysInput(self):
        validWeekdaysMsg = "Valid weekdays are: M T W TH F \n"
        validSelectDays = False
        while not validSelectDays:
            selectDays = raw_input("\n enter session weekdays: eg - M \t W,TH \t T,W,TH \t T,TH,F \n")
            validSelectDays = self.validateWeekdayInput(selectDays)
            if self.valueIsQuitOrExit(selectDays):
                break
            if not validSelectDays:
                print validWeekdaysMsg
        return selectDays

    def validateNumericalInput(self, inputValue):
        isNumerical = True
        try:
            inputValue = int(inputValue)
        except ValueError:
            print self.errorMsgPrefix + " %s entry isn't numerical" % inputValue
            isNumerical = False
        return inputValue, isNumerical

    def isValidMonth(self, inputMonth):
        return inputMonth in range(1,13)

    def validateWeekdayInput(self, inputValue):
        inputValueSet = set(inputValue.split(","))
        validWeekdaysSet = set(EXPECTED_ALL_WEEKDAYS_ABBREV)
        return len(inputValueSet.intersection(validWeekdaysSet)) == len(inputValueSet)

    def valueIsQuitOrExit(self, inputValue):
        isQuitOrExit = str(inputValue).lower() in ("quit", "exit")
        if isQuitOrExit:
            print "\n <<<<< exiting program >>>>> \n"
        return isQuitOrExit

    def runToGetStudentInfoAndSessionDates(self):
        print "\n this script will save the student(s) name & session dates for the same month, year \n"
        print ">> to exit at any time, enter 'quit' or 'exit' as the value w/o the single quotes \n"

        monthVal = self.getMonthValueInput()
        if self.valueIsQuitOrExit(monthVal):
            return
        yearVal = self.getYearValueInput()
        if self.valueIsQuitOrExit(yearVal):
            return
        print "\n will be getting dates for month %d, year %d \n" % (monthVal, yearVal)

        while True:
            studentName = self.getStudentNameInput()
            if self.valueIsQuitOrExit(studentName):
                break
            selectDays = self.getSelectDaysInput()
            if self.valueIsQuitOrExit(selectDays):
                break
            print "\n will be getting %s days for %s \n" % (selectDays, studentName)

            studentObj = StudentInfo(studentName, monthVal, yearVal, selectDays)
            self.studentList.append(studentObj.getStudentNameAndSessionDaysAndDates())

        print "\n ~~~~ total students entered: %d ~~~~ \n" % len(self.studentList)
        for s in self.studentList:
            print "\n student(s) : %s, total session dates retrieved: %d \n" % (s[0], len(s[1]))

        if self.checkStudentListHasValues():
            self.writeStudentDatesToFile()

    def checkStudentListHasValues(self):
        if self.studentList:
            return True
        print "\n No student session dates to retrieve, no data to write for! \n"

    def getWkdaysAbbrevSet(self, w):
        return ",".join(set([wkdy[0] for wkdy in w]))

    def convDateToMMDD(self, d):
        return d.strftime("%m/%d")

    def writeStudentDatesToFile(self):
        self.fileName = self.fileName % (self.month, self.year, datetime.datetime.now().strftime("%Y_%m_%d_%H-%M-%S"))
        print "\n attempting to write '%s'" % self.fileName

        self.studentDataStoreDict = StudentInfoDateStore(self.studentList).getStudentsDict()

        # print "\n ~~ writing %s using tabulate ~~ \n" % self.fileName
        self.writeStudentDatesToFileUsingTabulate()

    def writeStudentDatesToFileUsingTabulate(self):
        with open(self.fileName, "w") as f:
            f.write(self.fileName + " \n" + "--------"*7 + " \n\n")
            for studentName, sessDates in self.studentDataStoreDict.iteritems():
                studentInitials = [s[0] for s in studentName.split(";")]
                studentNameAndWkdays = [studentName + " - " + self.getWkdaysAbbrevSet(sessDates)]
                headerTitles = studentNameAndWkdays + studentInitials
                tableData = []
                for d in range(0, len(sessDates), 2):
                    twoDates = sessDates[d:d + 2]
                    twoDates = [(wkday, self.convDateToMMDD(dt)) for wkday, dt in twoDates]
                    # pool 2 dates together for display & whitespace for checklist per initial
                    rowData = [" - ".join([str(d) for d in twoDates])]
                    rowData += [" "]*len(studentInitials)
                    tableData.append(rowData)
                # see tbl formats here: https://bitbucket.org/astanin/python-tabulate
                tabulateData = tabulate(tableData, headers=headerTitles, tablefmt="presto")
                print tabulateData + "\n"
                f.write(tabulateData)
                f.write("\n"*3)
                print "\n -- wrote %s: %d session dates\n\n" % (studentName, len(sessDates))
        print "\n ** successfully wrote tabulated file '%s' ** \n" % self.fileName


if __name__ == "__main__":
    GenerateStudentSessionDates().runToGetStudentInfoAndSessionDates()
    print "\n\n ****** end program ****** "
