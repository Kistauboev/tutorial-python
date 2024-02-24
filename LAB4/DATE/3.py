from datetime import date, timedelta

today = date.today()

day = today - timedelta(days=5)

print(day)