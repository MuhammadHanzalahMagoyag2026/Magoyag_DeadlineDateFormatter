# Version 2: Formatted event deadline using the datetime module
from datetime import date

event_title = input("Enter event title: ").strip()
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

formatted_title = event_title.upper()
month_name = event_date.strftime("%B")
weekday_name = event_date.strftime("%A")
formatted_date = f"{month_name} {day}, {year}"

print("\nFormatted Output:")
print("Event:", formatted_title)
print("Date:", formatted_date)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday_name)

