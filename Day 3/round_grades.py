#write a program that modifies a list of marks
#round the marks


grades = [11.645,10,14.5,12.7,13.3,7.8,9.9999,16.6,15.5556]
i=0
for grade in grades:
    if type(grade) == float:
        if grade - int(grade) < 0.5:
            grades[i] = int(grade)              #change the number in the list: rounddown using cast method
        else:
            grades[i] = int(grade) + 1          #roundup
    if grade >= 16:
        grades[i] = str(grades[i]) + "(très bien)"
    elif grade >= 14:
        grades[i] = str(grades[i]) + "(bien)"
    elif grade >= 12:
        grades[i] = str(grades[i]) + "(assez bien)"
    elif grade >= 10:
        grades[i] = str(grades[i]) + "(sans mention)"
    else:
        grades[i] = str(grades[i]) + "(échec)"
    i += 1                                          #last instruction in the loop FOR
print(grades)