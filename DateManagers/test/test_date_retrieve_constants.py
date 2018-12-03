"""
Description: constants for test_date_retrieve
"""

import datetime


EXPECTED_ALL_WEEKDAYS = (0, 1, 2, 3, 4)  # 5, 6 are weekends


# select days T (1), TH (3), F (4)
EXPECTED_SELECT_WEEKDAYS = (1, 3, 4)


EXPECTED_DEC2018_DATES = (datetime.datetime(2018, 12, 1, 0, 0), datetime.datetime(2018, 12, 2, 0, 0), datetime.datetime(
    2018, 12, 3, 0, 0), datetime.datetime(2018, 12, 4, 0, 0), datetime.datetime(2018, 12, 5, 0, 0), datetime.datetime(2018, 12, 6, 0, 0), datetime.datetime(2018, 12, 7, 0, 0), datetime.datetime(2018, 12, 8, 0, 0), datetime.datetime(2018, 12, 9, 0, 0), datetime.datetime(2018, 12, 10, 0, 0), datetime.datetime(2018, 12, 11, 0, 0), datetime.datetime(2018, 12, 12, 0, 0), datetime.datetime(2018, 12, 13, 0, 0), datetime.datetime(2018, 12, 14, 0, 0), datetime.datetime(2018, 12, 15, 0, 0), datetime.datetime(2018, 12, 16, 0, 0), datetime.datetime(2018, 12, 17, 0, 0), datetime.datetime(2018, 12, 18, 0, 0), datetime.datetime(2018, 12, 19, 0, 0), datetime.datetime(2018, 12, 20, 0, 0), datetime.datetime(2018, 12, 21, 0, 0), datetime.datetime(2018, 12, 22, 0, 0), datetime.datetime(2018, 12, 23, 0, 0), datetime.datetime(2018, 12, 24, 0, 0), datetime.datetime(2018, 12, 25, 0, 0), datetime.datetime(2018, 12, 26, 0, 0), datetime.datetime(2018, 12, 27, 0, 0), datetime.datetime(2018, 12, 28, 0, 0), datetime.datetime(2018, 12, 29, 0, 0), datetime.datetime(2018, 12, 30, 0, 0), datetime.datetime(2018, 12, 31, 0, 0))


# from M-F (0..4) inclusive, no weekends
EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS = (((0, datetime.datetime(2018, 12, 3, 0, 0)), (1, datetime.datetime(2018, 12, 4, 0, 0)), (2, datetime.datetime(2018, 12, 5, 0, 0)), (3, datetime.datetime(2018, 12, 6, 0, 0)), (4, datetime.datetime(2018, 12, 7, 0, 0)), (0, datetime.datetime(2018, 12, 10, 0, 0)), (1, datetime.datetime(2018, 12, 11, 0, 0)), (2, datetime.datetime(2018, 12, 12, 0, 0)), (3, datetime.datetime(2018, 12, 13, 0, 0)), (4, datetime.datetime(2018, 12, 14, 0, 0)), (0, datetime.datetime(2018, 12, 17, 0, 0)), (1, datetime.datetime(2018, 12, 18, 0, 0)), (2, datetime.datetime(2018, 12, 19, 0, 0)), (3, datetime.datetime(2018, 12, 20, 0, 0)), (4, datetime.datetime(2018, 12, 21, 0, 0)), (0, datetime.datetime(2018, 12, 24, 0, 0)), (1, datetime.datetime(2018, 12, 25, 0, 0)), (2, datetime.datetime(2018, 12, 26, 0, 0)), (3, datetime.datetime(2018, 12, 27, 0, 0)), (4, datetime.datetime(2018, 12, 28, 0, 0)), (0, datetime.datetime(2018, 12, 31, 0, 0)))
)

# select days T (1), TH (3), F (4)
EXPECTED_DEC2018_SELECT_DATES_AND_WEEKDAYS = (((1, datetime.datetime(2018, 12, 4, 0, 0)), (3, datetime.datetime(2018, 12, 6, 0, 0)), (4, datetime.datetime(2018, 12, 7, 0, 0)), (1, datetime.datetime(2018, 12, 11, 0, 0)), (3, datetime.datetime(2018, 12, 13, 0, 0)), (4, datetime.datetime(2018, 12, 14, 0, 0)), (1, datetime.datetime(2018, 12, 18, 0, 0)), (3, datetime.datetime(2018, 12, 20, 0, 0)), (4, datetime.datetime(2018, 12, 21, 0, 0)), (1, datetime.datetime(2018, 12, 25, 0, 0)), (3, datetime.datetime(2018, 12, 27, 0, 0)), (4, datetime.datetime(2018, 12, 28, 0, 0)))
)