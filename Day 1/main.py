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


#exercise 3 - print "It's cold" when it's 0 or less degree; print "it's hot" otherwise
temperature = 5
if temperature <= 0 :
    print("It's cold.")
else:
    print("It's hot.")

#exercise 4 - student's grade

marks = 12
if marks >= 16:
    print("très bien")
elif marks >= 14:
    print("bien")
elif marks >= 12:
    print("assez bien")
elif marks >= 10:
    print("sans mention")
else:
    print("échec")


#exercise 5 - leap year

year = 2000
if (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0):
    print ("leap year")
else:
    print("common year")