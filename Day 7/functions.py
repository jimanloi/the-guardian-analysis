
"""
#Print()
result = print("hello")      #renvoie rien
print(result)               #elle renvoie None

#len()
number_of_users = len({"sylvain": "1234", "alice": "azerty"})
print(number_of_users)
"""

#définition des fonctions

def print_hello():
    print("hello")

def print_number_with_comma(number):
    float_value = float(number)
    integer_part = int(number)
    decimal_part = float_value - integer_part
    print(f"{integer_part},{str(decimal_part)[2:]}")

def square_number(x):
    result = x ** 2
    return result

#using the function
print_hello()                           #renvoie rien - value = None
print_number_with_comma(1.25)           #renvoie rien - value = None
result = print(square_number(4))        #result has a value
