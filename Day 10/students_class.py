#un program qui gère les stagiaires
from datetime import datetime
import csv

class Address:
    def __init__(self, _street, _street_number, _box, _city, _postcode, _country):
        self.street = _street
        self.street_number = _street_number
        self.box = _box
        self.postcode = _postcode
        self.city = _city
        self.country = _country

    def get_address(self):
        return (f"{self.street} {self.street_number}, {self.box}, {self.city}, {self.postcode}, {self.country}")

    def get_postcode(self):
        return (f"{self.postcode} {self.city}")

class Students:
    def __init__(self, _first_name, _family_name, _birth_date, _street, _street_number, _box, _city, _postcode, _country):
        self.first_name = _first_name
        self.family_name = _family_name
        self.birth_date = _birth_date = datetime.strptime(_birth_date,"%d/%m/%Y")
        self.address = Address(_street, _street_number, _box, _city, _postcode, _country)

    def get_age(self):
        today = datetime.today()
        birthday = self.birth_date.replace(year=today.year)
        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year

    def get_name(self):
        return self.first_name + " " + self.family_name

"""
if __name__ == "__main__":
    student1 = Students("Manloi","Jim","19/11/1996", "Rue Royale",150,"B3","Bruxelles",1000,"Belgique")
    print(student1.get_name())
    print(student1.address.get_address())
    print(student1.address.get_postcode())
    print(student1.get_age())
"""

#read csv file

list_of_students = []

with (open('stagiaires.csv', newline='') as csvfile):
    reader_students = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader_students)
    for row in reader_students:
        a_student = Students(row[1], row[0], row[2], row[3], row[4], row[5], row[7], row[6],row[8])
        list_of_students.append(a_student)

for student in list_of_students:
    print(f"{student.first_name}, {student.family_name}\n{student.address.get_address()}")

    """
    same as above:
    for i in range(len(students)):
    print(student.first_name, student.family_name)
    """

#average_age = 0
#for student in list_of_students:
#    average_age = average_age + (student.get_age()/len(list_of_students))
#print(average_age)

#age_of_ref = 35
#for student in list_of_students:
#    if student.get_age() > age_of_ref:
#        print(student.first_name + " is older than 35yo.")

#average age of students who live in Ixelles
total_age = 0
counter = 0
for student in list_of_students:
    if student.address.city == "Ixelles":
        counter += 1
        total_age += student.get_age()
print(total_age / counter)



#   print(list_of_students[2].get_name())
#   print(list_of_students[2].get_age())
#  print(list_of_students[2].address.get_address())
