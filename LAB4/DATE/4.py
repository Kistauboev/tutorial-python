from datetime import date, timedelta
today = date.today()
keshe = today - timedelta(days=1)
erten = today + timedelta(days=1)

print("Yesterday:", keshe)
print("Today:", today)
print("Tomorrow:", erten)