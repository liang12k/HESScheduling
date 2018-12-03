"""
Description: constants for test_date_retrieve
"""

import datetime


EXPECTED_ALL_WEEKDAYS = (0, 1, 2, 3, 4)  # 5, 6 are weekends


# select days T (1), TH (3), F (4)
EXPECTED_SELECT_WEEKDAYS_T_TH_F = (1, 3, 4)


EXPECTED_DEC2018_DATES = (datetime.date(2018, 12, 1), datetime.date(2018, 12, 2), datetime.date(2018, 12, 3), datetime.date(2018, 12, 4), datetime.date(2018, 12, 5), datetime.date(2018, 12, 6), datetime.date(2018, 12, 7), datetime.date(2018, 12, 8), datetime.date(2018, 12, 9), datetime.date(2018, 12, 10), datetime.date(2018, 12, 11), datetime.date(2018, 12, 12), datetime.date(2018, 12, 13), datetime.date(2018, 12, 14), datetime.date(2018, 12, 15), datetime.date(2018, 12, 16), datetime.date(2018, 12, 17), datetime.date(2018, 12, 18), datetime.date(2018, 12, 19), datetime.date(2018, 12, 20), datetime.date(2018, 12, 21), datetime.date(2018, 12, 22), datetime.date(2018, 12, 23), datetime.date(2018, 12, 24), datetime.date(2018, 12, 25), datetime.date(2018, 12, 26), datetime.date(2018, 12, 27), datetime.date(2018, 12, 28), datetime.date(2018, 12, 29), datetime.date(2018, 12, 30), datetime.date(2018, 12, 31))


# from M-F (0..4) inclusive, no weekends
EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS = (((0, datetime.date(2018, 12, 3)), (1, datetime.date(2018, 12, 4)), (2, datetime.date(2018, 12, 5)), (3, datetime.date(2018, 12, 6)), (4, datetime.date(2018, 12, 7)), (0, datetime.date(2018, 12, 10)), (1, datetime.date(2018, 12, 11)), (2, datetime.date(2018, 12, 12)), (3, datetime.date(2018, 12, 13)), (4, datetime.date(2018, 12, 14)), (0, datetime.date(2018, 12, 17)), (1, datetime.date(2018, 12, 18)), (2, datetime.date(2018, 12, 19)), (3, datetime.date(2018, 12, 20)), (4, datetime.date(2018, 12, 21)), (0, datetime.date(2018, 12, 24)), (1, datetime.date(2018, 12, 25)), (2, datetime.date(2018, 12, 26)), (3, datetime.date(2018, 12, 27)), (4, datetime.date(2018, 12, 28)), (0, datetime.date(2018, 12, 31)))
)

EXPECTED_DEC2018_ALL_DATES_AND_WEEKDAYS_WKDAY_ABBREV = ((("M", datetime.date(2018, 12, 3)), ("T", datetime.date(2018, 12, 4)), ("W", datetime.date(2018, 12, 5)), ("TH", datetime.date(2018, 12, 6)), ("F", datetime.date(2018, 12, 7)), ("M", datetime.date(2018, 12, 10)), ("T", datetime.date(2018, 12, 11)), ("W", datetime.date(2018, 12, 12)), ("TH", datetime.date(2018, 12, 13)), ("F", datetime.date(2018, 12, 14)), ("M", datetime.date(2018, 12, 17)), ("T", datetime.date(2018, 12, 18)), ("W", datetime.date(2018, 12, 19)), ("TH", datetime.date(2018, 12, 20)), ("F", datetime.date(2018, 12, 21)), ("M", datetime.date(2018, 12, 24)), ("T", datetime.date(2018, 12, 25)), ("W", datetime.date(2018, 12, 26)), ("TH", datetime.date(2018, 12, 27)), ("F", datetime.date(2018, 12, 28)), ("M", datetime.date(2018, 12, 31)))
)


# select days T (1), TH (3), F (4)
EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS = (((1, datetime.date(2018, 12, 4)), (3, datetime.date(2018, 12, 6)), (4, datetime.date(2018, 12, 7)), (1, datetime.date(2018, 12, 11)), (3, datetime.date(2018, 12, 13)), (4, datetime.date(2018, 12, 14)), (1, datetime.date(2018, 12, 18)), (3, datetime.date(2018, 12, 20)), (4, datetime.date(2018, 12, 21)), (1, datetime.date(2018, 12, 25)), (3, datetime.date(2018, 12, 27)), (4, datetime.date(2018, 12, 28)))
)

EXPECTED_DEC2018_SELECT_DATES_AND_T_TH_F_WEEKDAYS_WKDAY_ABBREV = ((("T", datetime.date(2018, 12, 4)), ("TH", datetime.date(2018, 12, 6)), ("F", datetime.date(2018, 12, 7)), ("T", datetime.date(2018, 12, 11)), ("TH", datetime.date(2018, 12, 13)), ("F", datetime.date(2018, 12, 14)), ("T", datetime.date(2018, 12, 18)), ("TH", datetime.date(2018, 12, 20)), ("F", datetime.date(2018, 12, 21)), ("T", datetime.date(2018, 12, 25)), ("TH", datetime.date(2018, 12, 27)), ("F", datetime.date(2018, 12, 28)))
)

# select days M (0), T (1), W (2)
EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS = ((0, datetime.date(2018, 12, 3)), (1, datetime.date(2018, 12, 4)), (2, datetime.date(2018, 12, 5)), (0, datetime.date(2018, 12, 10)), (1, datetime.date(2018, 12, 11)), (2, datetime.date(2018, 12, 12)), (0, datetime.date(2018, 12, 17)), (1, datetime.date(2018, 12, 18)), (2, datetime.date(2018, 12, 19)), (0, datetime.date(2018, 12, 24)), (1, datetime.date(2018, 12, 25)), (2, datetime.date(2018, 12, 26)), (0, datetime.date(2018, 12, 31)))


EXPECTED_DEC2018_SELECT_DATES_AND_M_T_W_WEEKDAYS_WKDAY_ABBREV = ((("M", datetime.date(2018, 12, 3)), ("T", datetime.date(2018, 12, 4)), ("W", datetime.date(2018, 12, 5)), ("M", datetime.date(2018, 12, 10)), ("T", datetime.date(2018, 12, 11)), ("W", datetime.date(2018, 12, 12)), ("M", datetime.date(2018, 12, 17)), ("T", datetime.date(2018, 12, 18)), ("W", datetime.date(2018, 12, 19)), ("M", datetime.date(2018, 12, 24)), ("T", datetime.date(2018, 12, 25)), ("W", datetime.date(2018, 12, 26)), ("M", datetime.date(2018, 12, 31)))
)