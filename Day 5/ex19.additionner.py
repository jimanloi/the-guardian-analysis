sum = 0

while True:
    to_add = float(input("type a value : "))
    if to_add:
        sum += to_add
        print(f"sum: {sum}")
    else:
        break
print(sum)