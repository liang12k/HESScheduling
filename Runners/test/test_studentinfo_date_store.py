"""
Description: tests studentinfo_date_store
"""

import unittest
from DateManagers.test.test_date_retrieve_constants import *
from Runners.studentinfo_date_store import StudentInfoDateStore
from StudentManager.student_info import StudentInfo


class TestStudentInfoDateStore(unittest.TestCase):
    def setUp(self):
        self.year = 2018
        self.novMonth = 11
        self.decMonth = 12
        self.student1NameNov2018 = "Tim"
        self.student1Nov2018SelDaysMWTHF = "M,W,TH,F"
        self.student1Obj = StudentInfo(self.student1NameNov2018, self.novMonth, self.year, self.student1Nov2018SelDaysMWTHF)
        self.student2NameNov2018 = "Alysha;Abduvoris"
        self.student2Nov2018SelDaysTTH = "T,TH"
        self.student2Obj = StudentInfo(self.student2NameNov2018, self.novMonth, self.year, self.student2Nov2018SelDaysTTH)
        self.student3NameNov2018 = "Aiden"
        self.student3Nov2018SelDaysM = "M"
        self.student3Obj = StudentInfo(self.student3NameNov2018, self.novMonth, self.year, self.student3Nov2018SelDaysM)
        self.student4NameDec2018 = "Ceylan"
        self.student4Dec2018SelDaysMTW = "M,T,W"
        self.student4Obj = StudentInfo(self.student4NameDec2018, self.decMonth, self.year, self.student4Dec2018SelDaysMTW)

    def getCombinationsList(self, listOfStudentObjs):
        """

        :param listOfStudentObjs: list of StudentInfo objs
        :return: list of StudentInfo.getStudentNameAndSessionDaysAndDates return values
        """
        studentsList = []
        for s in listOfStudentObjs:
            studentsList.append(s.getStudentNameAndSessionDaysAndDates())
        return studentsList

    def test_putStudentsListIntoDict_student1Nov2018SelDaysMWTHF_student2Nov2018SelDaysTTH(self):
        expectedDict = {
            "TIM": EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS_WKDAY_ABBREV,
            "ALYSHA;ABDUVORIS" : EXPECTED_NOV2018_SELECT_DATES_AND_T_TH_WEEKDAYS_WKDAY_ABBREV,
        }
        studentsList = [self.student1Obj, self.student2Obj]
        studentsData = StudentInfoDateStore(self.getCombinationsList(studentsList))
        self.assertDictEqual(
            expectedDict, studentsData.getStudentsDict()
        )

    def test_putStudentsListIntoDict_student1Nov2018SelDaysMWTHF_student3Nov2018SelDaysM(self):
        expectedDict = {
            "TIM": EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS_WKDAY_ABBREV,
            "AIDEN": EXPECTED_NOV2018_SELECT_DATES_AND_M_WEEKDAYS_WKDAY_ABBREV
        }
        studentsList = [self.student1Obj, self.student3Obj]
        studentsData = StudentInfoDateStore(self.getCombinationsList(studentsList))
        self.assertDictEqual(
            expectedDict, studentsData.getStudentsDict()
        )

    def test_putStudentsListIntoDict_student3Nov2018SelDaysM(self):
        expectedDict = {
            "AIDEN": EXPECTED_NOV2018_SELECT_DATES_AND_M_WEEKDAYS_WKDAY_ABBREV,
        }
        studentsList = [self.student3Obj]
        studentsData = StudentInfoDateStore(self.getCombinationsList(studentsList))
        self.assertDictEqual(
            expectedDict, studentsData.getStudentsDict()
        )

    def test_putStudentsListIntoDict_student4Dec2018SelDaysM(self):
        expectedDict = {
            "CEYLAN": EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS_WKDAY_ABBREV,
        }
        studentsList = [self.student4Obj]
        studentsData = StudentInfoDateStore(self.getCombinationsList(studentsList))
        self.assertDictEqual(
            expectedDict, studentsData.getStudentsDict()
        )

    # this isn't possible yet - combining diff months
    # but adding this test case here as a place holder TODO
    def test_putStudentsListIntoDict_student1Nov2018SelDaysMWTHF_student2Nov2018SelDaysTTH_student3Nov2018SelDaysM_student4Dec2018SelDaysM(self):
        expectedDict = {
            "TIM":              EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS_WKDAY_ABBREV,
            "ALYSHA;ABDUVORIS": EXPECTED_NOV2018_SELECT_DATES_AND_T_TH_WEEKDAYS_WKDAY_ABBREV,
            "AIDEN": EXPECTED_NOV2018_SELECT_DATES_AND_M_WEEKDAYS_WKDAY_ABBREV,
            "CEYLAN": EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS_WKDAY_ABBREV,
        }
        studentsList = [self.student1Obj, self.student2Obj, self.student3Obj, self.student4Obj]
        studentsData = StudentInfoDateStore(self.getCombinationsList(studentsList))
        self.assertDictEqual(
            expectedDict, studentsData.getStudentsDict()
        )


if __name__ == "__main__":
    unittest.main()