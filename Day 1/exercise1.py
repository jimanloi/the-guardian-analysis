#exercise 1 - calculate the surface area of a circle with a given diameter

import math
diameter = int(input("diameter (cm) : "))
circle_surface = (diameter/2) **2 * math.pi
rounded_number_cm = round(circle_surface,2)
rounded_number_m = (round(circle_surface/100,2))
print("surface area : " + str(rounded_number_cm) + " cm\u00b2" + "/" + str(rounded_number_m) + "m\u00b2")

#exercise 2 - translate seconds to hour:minute:second

total_second = int(input("number of second :"))
hour = (total_second//3600)
minute = ((total_second%3600)//60)
second = (total_second%60)
print(str(hour) + ":" + str(minute) + ":" + str(second))


#exercise 3 - number of days before your birthday

name = input("Name : ")
print("Your birth date?")
birth_day = input("Date : ")
birth_month = input("Month : ")
birth_year = input("Year : ")
from datetime import datetime
today = datetime.date(today)
print(today)

