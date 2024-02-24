from datetime import datetime
dt = datetime.now()
dt_without_microseconds = dt.replace(microsecond=0)

print(f"Original datetime: {dt}")
print(f"Datetime without microseconds: {dt_without_microseconds}")