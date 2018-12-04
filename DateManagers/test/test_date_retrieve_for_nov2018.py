"""
Description: tests date_retrieve for Nov2018
"""

import unittest
from DateManagers.date_retrieve import DateRetriever
from DateManagers.test.test_date_retrieve_constants import *


class TestNov2018_DateRetriever(unittest.TestCase):

    def setUp(self):
        self.month = 11
        self.year = 2018
        self.selectDays1 = "M,W,TH,F"
        self.selectDays2 = "T,TH"
        self.drObjDefault = DateRetriever(self.month, self.year)
        self.drObjSel1Days = DateRetriever(self.month, self.year, self.selectDays1)
        self.drObjSel2Days = DateRetriever(self.month, self.year, self.selectDays2)

    def test_parseSelectDays_no_selectDays_get_full_business_week(self):
        expectedDays = ["M", "T", "W", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjDefault.parseSelectDays(""))

    def test_parseSelectDays_entered_selectDays(self):
        expectedDays = ["M", "W", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjSel1Days.parseSelectDays(self.selectDays1))

    # ========== test NOV.2018 ==========================================
    def test_getAllDatesForMonth_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getAllDatesForMonth())

    def test_getAllDatesForMonth_forNOV2018_with_selectDays_M_W_TH_F(self):
        # gets all the dates using func 'getAllDatesForMonth'
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSel1Days.getAllDatesForMonth())

    def test_getSelectDaysAsInt_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_ALL_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forNOV2018_with_selectDays_M_W_TH_F(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_M_W_TH_F
        self.assertTupleEqual(expectedTuple, self.drObjSel1Days.getSelectDaysAsInt())

    def test_getDatesForSelectDays_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_ALL_DATES_AND_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getDatesForSelectDays())

    def test_getDatesForSelectDays_forNOV2018_with_selectDays_M_W_TH_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSel1Days.getDatesForSelectDays())

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjDefault.getDatesForSelectDaysInWeekdayAbbrev())

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_with_selectDays_T_TH_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSel1Days.getDatesForSelectDaysInWeekdayAbbrev()
        )



if __name__ == "__main__":
    unittest.main()