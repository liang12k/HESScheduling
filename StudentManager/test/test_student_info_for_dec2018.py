"""
Description: test student_info for Dec2018
"""

import unittest
from StudentManager.test.test_student_info_constants import *
from StudentManager.student_info import StudentInfo


class TestDec2018_StudentInfo(unittest.TestCase):
    def setUp(self):
        self.decMonth = 12
        self.year2018 = 2018
        self.student1Name = "Ceylan"
        self.selectDaysMTW = "M,T,W"
        self.student1DefDays = StudentInfo(self.student1Name, self.decMonth, self.year2018)
        self.student1SelDays = StudentInfo(self.student1Name, self.decMonth, self.year2018, self.selectDaysMTW)
        self.student2Name = "Evelyn"
        self.selectDaysTTHF = "T,TH,F"
        self.student2DefDays = StudentInfo(self.student2Name, self.decMonth, self.year2018)
        self.student2SelDays = StudentInfo(self.student2Name, self.decMonth, self.year2018, self.selectDaysTTHF)
        # TODO for additional tesing of diff month, year, days in diff class
        # self.selectDaysTTHF = "T,TH,F"
        # self.student3DefDays = StudentInfo(self.decMonth, self.year2018)
        # self.student3SelDays = StudentInfo(self.decMonth, self.year2018, self.selectDaysTTHF)

    def test_getSessionDaysAndDates_unspecified_sessionDates_for_student1DefDays(self):
        expectedOutput = tuple(EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS)
        self.assertTupleEqual(expectedOutput, self.student1DefDays.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_specified_sessionDates_for_student1SelDays(self):
        expectedOutput = tuple(EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS)
        self.assertTupleEqual(expectedOutput, self.student1SelDays.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_unspecified_sessionDates_for_student2DefDays(self):
        expectedOutput = tuple(EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS)
        self.assertTupleEqual(expectedOutput, self.student2DefDays.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_specified_sessionDates_for_student2SelDays(self):
        expectedOutput = tuple(EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS)
        self.assertTupleEqual(expectedOutput, self.student2SelDays.getSessionDaysAndDates())


if __name__ == "__main__":
    unittest.main()