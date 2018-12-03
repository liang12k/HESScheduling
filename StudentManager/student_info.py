"""
Description: student name and their info
"""

import logging
from pprint import pprint, pformat
from DateManagers.date_retrieve import DateRetriever

logging.getLogger().setLevel(logging.INFO)


class StudentInfo(object):
    def __init__(self, name, sessionMonth, sessionYear, sessionDays=""):
        self.name = name
        self.sessionDaysToParse = sessionDays
        self.sessionMonth = sessionMonth
        self.sessionYear = sessionYear
        self.dateRetriever = DateRetriever(self.sessionMonth, self.sessionYear, self.sessionDaysToParse)

    def getSessionDaysAndDates(self):
        sessionDayAndDates = self.dateRetriever.getDatesForSelectDays()
        logging.info("For %s, session dates: \n %s", self.name, pformat(sessionDayAndDates))
        return sessionDayAndDates


if __name__ == "__main__":
    pass