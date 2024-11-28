#write a programme that shows the grade of a student
#if more than and equal to 16 : très bien
#more than and equal to  14 and less than 16: bien
#more than and equal to  12 and less than 14: assez bien
#more than and equal to  10 and less than 12: sans mention
#less than 10: échec

marks = 12

#version 1 w/ IF, ELIF, ELSE

"""
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
"""

#version 2 w/ only IF
if marks >= 16:
    print("très bien")
if 14 <= marks < 16:    #marks >= 14 and marks < 16:
    print("bien")
if 12 <= marks < 14:    #marks >= 12 and marks < 14:
    print("assez bien")
if 10 <= marks < 12:    #marks >= 10 and marks < 12:
    print("sans mention")
if marks < 10:
    print("échec")

