"""
Description: tests date_retrieve
"""

import unittest
import datetime, calendar
from DateManagers.date_retrieve import DateRetriever


EXPECTED_DEC2018 = (datetime.datetime(2018, 12, 1, 0, 0), datetime.datetime(2018, 12, 2, 0, 0), datetime.datetime(
    2018, 12, 3, 0, 0), datetime.datetime(2018, 12, 4, 0, 0), datetime.datetime(2018, 12, 5, 0, 0), datetime.datetime(2018, 12, 6, 0, 0), datetime.datetime(2018, 12, 7, 0, 0), datetime.datetime(2018, 12, 8, 0, 0), datetime.datetime(2018, 12, 9, 0, 0), datetime.datetime(2018, 12, 10, 0, 0), datetime.datetime(2018, 12, 11, 0, 0), datetime.datetime(2018, 12, 12, 0, 0), datetime.datetime(2018, 12, 13, 0, 0), datetime.datetime(2018, 12, 14, 0, 0), datetime.datetime(2018, 12, 15, 0, 0), datetime.datetime(2018, 12, 16, 0, 0), datetime.datetime(2018, 12, 17, 0, 0), datetime.datetime(2018, 12, 18, 0, 0), datetime.datetime(2018, 12, 19, 0, 0), datetime.datetime(2018, 12, 20, 0, 0), datetime.datetime(2018, 12, 21, 0, 0), datetime.datetime(2018, 12, 22, 0, 0), datetime.datetime(2018, 12, 23, 0, 0), datetime.datetime(2018, 12, 24, 0, 0), datetime.datetime(2018, 12, 25, 0, 0), datetime.datetime(2018, 12, 26, 0, 0), datetime.datetime(2018, 12, 27, 0, 0), datetime.datetime(2018, 12, 28, 0, 0), datetime.datetime(2018, 12, 29, 0, 0), datetime.datetime(2018, 12, 30, 0, 0), datetime.datetime(2018, 12, 31, 0, 0))


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

    def test_getAllDatesForMonth_no_selectDays(self):
        expectedTuple = EXPECTED_DEC2018
        self.assertTupleEqual(expectedTuple, self.drObjDefault.getAllDatesForMonth())

    def test_getAllDatesForMonth_with_selectDays(self):
        expectedTuple = EXPECTED_DEC2018
        self.assertTupleEqual(expectedTuple, self.drObjSelDays.getAllDatesForMonth())


if __name__ == "__main__":
    unittest.main()