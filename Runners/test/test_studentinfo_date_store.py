"""
Description: tests studentinfo_date_store
"""

import unittest
from Runners.studentinfo_date_store import StudentInfoDateStore


class TestStudentInfoDateStore(unittest.TestCase):
    def setUp(self):
        self.year = 2018
        self.novMonth = 11
        self.decMonth = 12
        self.student1 = ""
        self.student1SelDaysMWTHF = "M,W,TH,F"
        self.student2 = ""
        self.student2SelDaysTTH = "T,TH"
        self.student3 = ""
        self.student3SelDaysMTW = "M,T,W"
        self.student4 = ""
        self.student4SelDaysM = "M"

    def test_putStudentsListIntoDict(self):
        pass


if __name__ == "__main__":
    unittest.main()