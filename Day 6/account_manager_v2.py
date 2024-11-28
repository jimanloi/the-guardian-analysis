"""
Upgrade par rapport à la v1 :
Au démarrage, le programme doit lire le fichier accounts.txt
et "importer" les comptes (un compte par ligne dans le fichier).
Et avant la fermeture du programme, ce dernier doit MàJ le fichier texte.
"""

accounts = {}

with open("accounts.txt", "r") as fp:
    for line in fp:
        username,password = line.strip().split(": ")
        accounts[username] = password
        print(line[:-1])

while True:
    print(f"1 - Create an account\n2 - Modify a password\n3 - Remove an account\n4 - Show all usernames\n5 - end the session")
    action = input("Action (enter the number): ")
    if action == "1":                                            #Create an account
        username = input(f"To create an account.\nusername : ")  # Enter a new username
        if username not in accounts:
            accounts.setdefault(username)                       # Create a new user
            accounts[username] = input("password : ")           # Enter a new password
        else:
            print("Username already exists.")
    elif action == "2":                                             #Modify a password
        username = input(f"To modify your password.\nenter your username: ")
        if accounts.get(username, " ") != " ":                    #if the username is valid
            password = input("enter your old password : ")
            if password == accounts.get(username):
                password = input("enter a new password : ")
                accounts[username] = password
            else:
                print("Wrong old password.")
        if accounts.get(username, " ") == " ":              #if the username is not in the dictionnary
            print(f"Invalid username. Please choose the action again.")
    elif action == "3":                                       #To remove an account
        username = input(f"To remove your account.\nenter your username: ")
        if accounts.get(username, " ") != " ":                  #if the username is valid
            password = input("enter your password : ")
            while password != accounts.get(username):
                password = input("Wrong password. Re-enter your password : ")
            if password == accounts.get(username):                 #if the password is valid
                del accounts[username]
                print("account deleted.")
        else:
            print(f"Invalid username. Please choose the action again.")
    elif action == "4":
        for account in accounts:
            print(account)
    elif action == "5":
        with open("accounts.txt", "w") as fp:
            for username, password in accounts.items():
                fp.write(f"{username}: {password}\n")
        break
    else:
        print("Incorrect input.")
print("Program exited.")
print(accounts)