#un program qui gère les stagiaires
from datetime import date, datetime

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

if __name__ == "__main__":
    student1 = Students("Manloi","Jim","19/11/1996", "Rue Royale",150,"B3","Bruxelles",1000,"Belgique")
    print(student1.get_name())
    print(student1.address.get_address())
    print(student1.address.get_postcode())
    print(student1.get_age())