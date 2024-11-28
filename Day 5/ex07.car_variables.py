"""Based on the following data:

    There are 100 cars available.
    Each car has 4 seats (driver included)
    There are 35 drivers
    There are 120 passengers

Answer the following questions:

    How many cars are available ?
    How many drivers are available ?
    How many cars won't be used ?
    How many passengers can be transported during each travel ?
    How many passengers will have to wait next turn ?
    How many travels would be necessary to transport all passengers ?

Keep in mind that the principe should be to store each answer (the number only) in a dedicated variable."""

available_cars = 100
seats_per_car = 4
available_drivers = 35
passengers = 120

print(f"How many cars are available ? {available_cars}")
print(f"How many drivers are available ? {available_drivers}")
print(f"How many cars won't be used ? {available_cars-available_drivers}")
print(f"How many passengers can be transported during each travel ? {seats_per_car}")
