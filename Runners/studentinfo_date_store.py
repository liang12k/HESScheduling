"""
Description: holds student info and select session dates
"""
import logging
from StudentManager.student_info import StudentInfo

logging.getLogger().setLevel(logging.INFO)


class StudentInfoDateStore(object):
    def __init__(self, studentsList=None):
        """

        :param studentsList: list of tuples, eg: [(st1,"M,W"), (st2,"T,TH,F"), ...]
                             each tuple is a return of StudentInfo.getStudentNameAndSessionDaysAndDates
        """
        self.allStudentsDict = {}
        self.studentsList = studentsList or []
        self.putStudentsListIntoDict()

    def putStudentsListIntoDict(self):
        """
        updates the dict to hold student name and their respective session dates
        """
        for s in self.studentsList:
            name, sessionDates = s
            self.allStudentsDict[name.upper()] = sessionDates

    def getStudentsDict(self):
        return self.allStudentsDict


if __name__ == "__main__":
    pass