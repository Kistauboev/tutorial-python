from datetime import datetime

def date_diff_in_seconds(date1, date2):
  if not isinstance(date1, datetime) or not isinstance(date2, datetime):
    raise TypeError("date1 and date2 must be datetime objects.")

  time_delta = date2 - date1
  return time_delta.total_seconds()

date1 = datetime(2024, 2, 24, 12, 0, 0) 
date2 = datetime(2024, 2, 25, 10, 30, 0)

difference_in_seconds = date_diff_in_seconds(date1, date2)
print(difference_in_seconds)