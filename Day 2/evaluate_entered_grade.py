given_grade = float(input("Enter your marks (0 - 20) : "))

while not 0 <= given_grade <= 20 :
    given_grade = float(input("Re-enter your marks (0 - 20) : "))

if given_grade >= 16:
    print("très bien")
elif given_grade >= 14:
    print("bien")
elif given_grade >= 12:
    print("assez bien")
elif given_grade >= 10:
  print("sans mention")
else:
  print("échec")