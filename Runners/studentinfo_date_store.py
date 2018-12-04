"""
Description: holds student info and select session dates
"""
import logging
from StudentManager.student_info import StudentInfo

logging.getLogger().setLevel(logging.INFO)


class StudentInfoDateStore(object):
    def __init__(self, studentsList):
        """

        :param studentsList: list of tuples, eg: [(st1,"M,W"), (st2,"T,TH,F"), ...]
        """
        self.allStudentsDict = {}
        self.studentsList = studentsList
        self.putStudentsListIntoDict()

    def putStudentsListIntoDict(self):
        pass


if __name__ == "__main__":
    pass