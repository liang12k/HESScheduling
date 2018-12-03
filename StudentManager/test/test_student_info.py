"""
Description: test student_info
"""

import unittest
from StudentManager.test.test_student_info_constants import *
from StudentManager.student_info import StudentInfo


class TestStudentInfo(unittest.TestCase):
    def setUp(self):
        self.decMonth = 12
        self.year2018 = 2018
        self.selectDaysMTW = "M,T,W"
        self.student1DefDays = StudentInfo(self.decMonth, self.year2018)
        self.student1SelDays = StudentInfo(self.decMonth, self.year2018, self.selectDaysMTW)
        self.selectDaysTTHF = "T,TH,F"
        self.student2DefDays = StudentInfo(self.decMonth, self.year2018)
        self.student2SelDays = StudentInfo(self.decMonth, self.year2018, self.selectDaysTTHF)
        # TODO for additional tesing of diff month, year, days
        # self.selectDaysTTHF = "T,TH,F"
        # self.student2DefDays = StudentInfo(self.decMonth, self.year2018)
        # self.student2SelDays = StudentInfo(self.decMonth, self.year2018, self.selectDaysTTHF)

    def test_getSessionDaysAndDates_unspecified_sessionDates(self):
        pass

    def test_getSessionDaysAndDates_specified_sessionDates(self):
        pass


if __name__ == "__main__":
    unittest.main()