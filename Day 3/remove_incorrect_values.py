#remove incorrect values from a list of marks
#correct values = 0-20
#creat a new list and print a list of correct grades

grades = [-1,20,10,0,60,"14",7.5,"dix",12,True,13,False,16.5]
correct_grades = []
i=0
for correct_grade in grades:
    if (type(correct_grade) == int or type(correct_grade) == float) and 0 <= correct_grade <= 20:
        correct_grades.append(correct_grade)
    i += 1
print(correct_grades)