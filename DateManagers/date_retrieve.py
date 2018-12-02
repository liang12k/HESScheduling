"""
Description: handles getting available dates and their days based on month, year
"""

import datetime, calendar
import logging

WEEKDAY_TO_INT = {
    "M" : 0, "T": 1, "W": 2, "TH": 3, "F": 4, "SAT": 5, "SUN": 6
}


class DateRetriever(object):
    def __init__(self, month, year, selectDaysToParse=""):
        self.month = month
        self.year = year
        self.selectDays = self.parseSelectDays(selectDaysToParse)

    def parseSelectDays(self, selectDaysToParse):
        selDays = ["M", "T", "W", "TH", "F"]  # not incl weekends for now
        if not selectDaysToParse:
            logging.warning("*** Getting Mon.-Fri. weekdays! ***")
        else:
            selDays = selectDaysToParse.split(",")
        return selDays

    def getAllDatesForMonth(self):
        allDates = calendar.monthrange(self.year, self.month)
        # idx 1 gets count of all the days; do +1 in range to make last day inclusive
        allDates = tuple(datetime.datetime(self.year, self.month, d) for d in range(1, allDates[1] + 1))
        return allDates


if __name__ == "__main__":
    pass