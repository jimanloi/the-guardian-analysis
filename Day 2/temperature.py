# Exercise 1 - print "It's cold" when it's 0 or less degree; print "it's hot" otherwise

temperature = 20.5

"""
if temperature <= 0 :
    print("It's cold.")
else:
    print("It's hot.")
    """

if temperature < 0 :
    print("It's cold.")
elif temperature == 0 :
    print("Temperature is null.")
else:
    print("It's hot.")