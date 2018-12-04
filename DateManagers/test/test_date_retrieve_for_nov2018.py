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
        self.drObjDefault = DateRetriever(self.month, self.year)  # all weekdays
        self.selectDaysMWTHF = "M,W,TH,F"
        self.selectDaysMWF = "M,W,F"
        self.selectDaysTTH = "T,TH"
        self.selectDaysM = "M"
        self.drObjSelDaysMWTHF = DateRetriever(self.month, self.year, self.selectDaysMWTHF)
        self.drObjSelDaysMWF = DateRetriever(self.month, self.year, self.selectDaysMWF)
        self.drObjSelDaysTTH = DateRetriever(self.month, self.year, self.selectDaysTTH)
        self.drObjSelDaysM = DateRetriever(self.month, self.year, self.selectDaysM)

    def test_parseSelectDays_no_selectDays_get_full_business_week(self):
        expectedDays = ["M", "T", "W", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjDefault.parseSelectDays(""))

    def test_parseSelectDays_entered_selectDays(self):
        expectedDays = ["M", "W", "TH", "F"]
        self.assertEqual(expectedDays, self.drObjSelDaysMWTHF.parseSelectDays(self.selectDaysMWTHF))

    # ========== test NOV.2018 ==========================================
    def test_getAllDatesForMonth_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getAllDatesForMonth())

    def test_getAllDatesForMonth_forNOV2018_with_selectDays_M_W_TH_F(self):
        # gets all the dates using func 'getAllDatesForMonth'
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWTHF.getAllDatesForMonth())

    def test_getAllDatesForMonth_forNOV2018_with_selectDays_M_W_F(self):
        # gets all the dates using func 'getAllDatesForMonth'
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWF.getAllDatesForMonth())

    def test_getAllDatesForMonth_forNOV2018_with_selectDays_T_TH(self):
        # gets all the dates using func 'getAllDatesForMonth'
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysTTH.getAllDatesForMonth())

    def test_getAllDatesForMonth_forNOV2018_with_selectDays_M(self):
        # gets all the dates using func 'getAllDatesForMonth'
        expectedTuple = EXPECTED_NOV2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysM.getAllDatesForMonth())

    # ``````````````````````````````````````````````````````````````````````
    def test_getSelectDaysAsInt_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_ALL_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forNOV2018_with_selectDays_M_W_TH_F(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_M_W_TH_F
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWTHF.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forNOV2018_with_selectDays_M_W_F(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_M_W_F
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWF.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forNOV2018_with_selectDays_T_TH(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_T_TH
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysTTH.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forNOV2018_with_selectDays_M(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS_M
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysM.getSelectDaysAsInt())

    # ``````````````````````````````````````````````````````````````````````
    def test_getDatesForSelectDays_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_ALL_DATES_AND_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getDatesForSelectDays())

    def test_getDatesForSelectDays_forNOV2018_with_selectDays_M_W_TH_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWTHF.getDatesForSelectDays())

    def test_getDatesForSelectDays_forNOV2018_with_selectDays_M_W_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_F_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysMWF.getDatesForSelectDays())

    def test_getDatesForSelectDays_forNOV2018_with_selectDays_T_TH(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_T_TH_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysTTH.getDatesForSelectDays())

    def test_getDatesForSelectDays_forNOV2018_with_selectDays_M(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDaysM.getDatesForSelectDays())

    # ``````````````````````````````````````````````````````````````````````
    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_no_selectDays(self):
        expectedTuple = EXPECTED_NOV2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjDefault.getDatesForSelectDaysInWeekdayAbbrev())

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_with_selectDays_M_W_TH_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_TH_F_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSelDaysMWTHF.getDatesForSelectDaysInWeekdayAbbrev()
        )

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_with_selectDays_M_W_F(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_W_F_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSelDaysMWF.getDatesForSelectDaysInWeekdayAbbrev()
        )

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_with_selectDays_T_TH(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_T_TH_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSelDaysTTH.getDatesForSelectDaysInWeekdayAbbrev()
        )

    def test_getDatesForSelectDaysInWeekdayAbbrev_forNOV2018_with_selectDays_M(self):
        expectedTuple = EXPECTED_NOV2018_SELECT_DATES_AND_M_WEEKDAYS_WKDAY_ABBREV
        self.assertTupleEqual(
            expectedTuple,
            self.drObjSelDaysM.getDatesForSelectDaysInWeekdayAbbrev()
        )


if __name__ == "__main__":
    unittest.main()