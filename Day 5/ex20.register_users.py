max_number_users = 5
list_users = []

while True:
    if max_number_users > 0:
        user_input = input("Enter your name : ")
        if not user_input:
            print("invalid input.")
            continue
        list_users.append(user_input)
        print(list_users)
        max_number_users -= 1
    else:
        break
print(f"The final list : {list_users}")