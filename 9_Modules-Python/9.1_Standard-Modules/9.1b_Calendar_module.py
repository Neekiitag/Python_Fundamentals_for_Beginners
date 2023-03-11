import calendar

star = dir(calendar)
print(star)

cal = calendar.month(1992,10)
print(cal)

#checking if a year is a leap or not
if calendar.isleap(1992):
    print("This is a Leap Year")
else:
    print("This is not a leap year")