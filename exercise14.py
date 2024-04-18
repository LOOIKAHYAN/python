from datetime import date

first_date = date(2014,7,2)
last_date = date(2014,7,11)
days = last_date - first_date

print(days.days)