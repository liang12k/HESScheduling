"""
Description: tests date_retrieve
"""

import unittest
from DateManagers.date_retrieve import DateRetriever
from DateManagers.test.test_date_retrieve_constants import *


class TestDateRetriever(unittest.TestCase):

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

    def test_getAllDatesForMonth_forDEC2018_with_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_DATES
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getAllDatesForMonth())

    def test_getSelectDaysAsInt_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_ALL_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getSelectDaysAsInt())

    def test_getSelectDaysAsInt_forDEC2018_with_selectDays(self):
        expectedTuple = EXPECTED_SELECT_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getSelectDaysAsInt())

    def test_getDatesForSelectDays_forDEC2018_no_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getDatesForSelectDays())

    def test_getDatesForSelectDays_forDEC2018_with_selectDays(self):
        expectedTuple = EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getDatesForSelectDays())


if __name__ == "__main__":
    unittest.main()