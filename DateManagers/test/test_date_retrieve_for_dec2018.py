"""
Description: tests date_retrieve for Dec2018
"""

import unittest
from DateManagers.date_retrieve import DateRetriever
from DateManagers.test.test_date_retrieve_constants import *


class TestDec2018_DateRetriever(unittest.TestCase):

    def setUp(self):
        self.month = 12
        self.year = 2018
        self.selectDays = "T,TH,F"
        self.drObjDefault = DateRetriever(self.month, self.year)
        self.drObjSelDays = DateRetriever(self.month, self.year, self.selectDays)

    def test_parseSelectDays_no_selectDays_get_full_business_week(self):
        expectedDays = ["M", "T", "W", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjDefault.parseSelectDays(""))

    def test_parseSelectDays_entered_selectDays(self):
        expectedDays = ["T", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjSelDays.parseSelectDays(self.selectDays))

    # ========== test DEC.2018 ==========================================
    def test_getAllDatesForMonth_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getAllDatesForMonth())

    def test_getAllDatesForMonth_forDEC2018_with_selectDays_T_TH_F(self):
        expectedTuple = EXPECTED_DEC2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getAllDatesForMonth())

    def test_getSelectDaysAsInt_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_ALL_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forDEC2018_with_selectDays_T_TH_F(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_T_TH_F
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getSelectDaysAsInt())

    def test_getDatesForSelectDays_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getDatesForSelectDays())

    def test_getDatesForSelectDays_forDEC2018_with_selectDays_T_TH_F(self):
        expectedTuple = EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getDatesForSelectDays())

    def test_getDatesForSelectDaysInWeekdayAbbrev_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjDefault.getDatesForSelectDaysInWeekdayAbbrev())

    def test_getDatesForSelectDaysInWeekdayAbbrev_forDEC2018_with_selectDays_T_TH_F(self):
        expectedTuple = EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSelDays.getDatesForSelectDaysInWeekdayAbbrev()
        )



if __name__ == "__main__":
    unittest.main()