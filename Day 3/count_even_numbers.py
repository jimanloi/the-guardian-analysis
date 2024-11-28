#Write a programme that counts the number of even numbers.
#from a list

numbers = [1,2,46,71,69,44,43,22,14,88,13,14,60]
counter = 0
for even_number in numbers:
    if even_number % 2 == 0:
        counter += 1
        
print(f"The number of even numbers in the list: {counter}")
