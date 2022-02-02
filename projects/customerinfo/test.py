from datetime import datetime, date

today = datetime.now()
d = date(2021, 4, 18)

print(today)
print(today.strftime("%B %d, %Y"))

print(d)
print(d.strftime("%B %d, %Y"))
