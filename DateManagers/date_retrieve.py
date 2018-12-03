"""
Description: handles getting available dates and their days based on month, year
"""

import datetime, calendar
import logging

logging.getLogger().setLevel(logging.INFO)

WEEKDAY_TO_INT = {
    "M" : 0, "T": 1, "W": 2, "TH": 3, "F": 4, "SAT": 5, "SUN": 6
}


class DateRetriever(object):
    def __init__(self, month, year, selectDaysToParse=""):
        self.month = month
        self.year = year
        self.selectDays = self.parseSelectDays(selectDaysToParse)
        self.selectDaysAsInts = self.getSelectDaysAsInt()
        self.allDates = self.getAllDatesForMonth()

    def parseSelectDays(self, selectDaysToParse):
        selDays = ["M", "T", "W", "TH", "F"]  # not incl weekends for now
        if not selectDaysToParse:
            logging.warning("*** Getting Mon.-Fri. weekdays! *** \n")
        else:
            selDays = selectDaysToParse.upper().split(",")
            logging.info("*** Getting %s \n", str(selDays))
        return selDays

    def getSelectDaysAsInt(self):
        daysAsInt = tuple(WEEKDAY_TO_INT[s] for s in self.selectDays)
        return daysAsInt

    def getAllDatesForMonth(self):
        allDates = calendar.monthrange(self.year, self.month)
        # idx 1 gets count of all the days; do +1 in range to make last day inclusive
        allDates = tuple(datetime.datetime(self.year, self.month, d) for d in range(1, allDates[1] + 1))
        logging.info("\t there are %d days for month %d, year %d \n",
                     len(allDates), self.month, self.year)
        return allDates

    def getDatesForSelectDays(self):
        selectDates = self.allDates
        selectDates = tuple((a.weekday(), a) for a in selectDates if a.weekday() in self.selectDaysAsInts)
        logging.info("\t %d select days for month %d, year %d \n",
                     len(selectDates), self.month, self.year)
        return selectDates


if __name__ == "__main__":
    pass