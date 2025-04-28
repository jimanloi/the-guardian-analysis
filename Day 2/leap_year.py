year = 2000
if (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0):
    print ("leap year")
else:
    print("common year")


if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):  # != differnt than
    print ("leap year")
else:
    print("common year")


if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("common year")