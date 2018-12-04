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
        self.student1SelDaysMTW = StudentInfo(self.student1Name, self.decMonth, self.year2018, self.selectDaysMTW)
        self.student2Name = "Evelyn"
        self.selectDaysTTHF = "T,TH,F"
        self.student2DefDays = StudentInfo(self.student2Name, self.decMonth, self.year2018)
        self.student2SelDaysTTHF = StudentInfo(self.student2Name, self.decMonth, self.year2018, self.selectDaysTTHF)
        # TODO for additional tesing of diff month, year, days in diff class
        # self.selectDaysTTHF = "T,TH,F"
        # self.student3DefDays = StudentInfo(self.decMonth, self.year2018)
        # self.student3SelDays = StudentInfo(self.decMonth, self.year2018, self.selectDaysTTHF)

    def test_getStudentName_nameOf_student1DefDays(self):
        self.assertEqual(self.student1Name, self.student1DefDays.getStudentName())

    def test_getStudentName_nameOf_student1SelDaysMTW(self):
        self.assertEqual(self.student1Name, self.student1SelDaysMTW.getStudentName())

    def test_getStudentName_nameOf_student2DefDays(self):
        self.assertEqual(self.student2Name, self.student2DefDays.getStudentName())

    def test_getStudentName_nameOf_student2SelDaysTTHF(self):
        self.assertEqual(self.student2Name, self.student2SelDaysTTHF.getStudentName())

    def test_getSessionDaysAndDates_unspecified_sessionDates_for_student1DefDays(self):
        expectedOutput = EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(expectedOutput, self.student1DefDays.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_specified_sessionDates_for_student1SelDaysMTW(self):
        expectedOutput = EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(expectedOutput, self.student1SelDaysMTW.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_unspecified_sessionDates_for_student2DefDays(self):
        expectedOutput = EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(expectedOutput, self.student2DefDays.getSessionDaysAndDates())

    def test_getSessionDaysAndDates_specified_sessionDates_for_student2SelDaysTTHF(self):
        expectedOutput = EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(expectedOutput, self.student2SelDaysTTHF.getSessionDaysAndDates())

    def test_getStudentNameAndSessionDaysAndDates_unspecified_sessionDates_for_student1DefDays(self):
        expectedOutput = ("Ceylan", EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV)
        self.assertTupleEqual(expectedOutput, self.student1DefDays.getStudentNameAndSessionDaysAndDates())

    def test_getStudentNameAndSessionDaysAndDates_unspecified_sessionDates_for_student1SelDaysMTW(self):
        expectedOutput = ("Ceylan", EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS_WKDAY_ABBREV)
        self.assertTupleEqual(expectedOutput, self.student1SelDaysMTW.getStudentNameAndSessionDaysAndDates())

    def test_getStudentNameAndSessionDaysAndDates_unspecified_sessionDates_for_student2DefDays(self):
        expectedOutput = ("Evelyn", EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV)
        self.assertTupleEqual(expectedOutput, self.student2DefDays.getStudentNameAndSessionDaysAndDates())

    def test_getStudentNameAndSessionDaysAndDates_unspecified_sessionDates_for_student2SelDaysTTHF(self):
        expectedOutput = ("Evelyn", EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS_WKDAY_ABBREV)
        self.assertTupleEqual(expectedOutput, self.student2SelDaysTTHF.getStudentNameAndSessionDaysAndDates())


if __name__ == "__main__":
    unittest.main()