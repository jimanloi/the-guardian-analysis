#example with students' grade

grades = [10,8,14,20,17,15,7,5,16,18]
print(grades[0:-2])

fifth_grade = grades[4]     #lecture de la 5e élément
grades[4] = 19              #modification du 5e élément
print(grades)
print(fifth_grade)            #fifth_grade still refers to 17

#example with random things

random_list = [1,"hello",True,45.8,"world"]
print(random_list[0:])