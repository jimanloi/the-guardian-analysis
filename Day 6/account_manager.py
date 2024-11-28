"""
objectif: créer un programme utilisable via la console permettant de
- créer un compt (paire username: password)
- modifier un mot de passe d'un compte existant
- supprimer un compte
- afficher la liste de tous les pseudos (un par ligne)
le programme doit demander en boucle (tant que l'on ne souhaite pas quitter)
"""

accounts = {}

while True:
    print(f"1 - Create an account\n2 - Modify a password\n3 - Remove an account\n4 - Show all usernames\n5 - end the session")
    action = input("Action (enter the number): ")
    if action == "1":                                            #Create an account
        username = input(f"To create an account.\nusername : ")      #Enter a new username
        if username not in accounts:
            accounts.setdefault(username)                              #Create a new user
            accounts[username] = input("password : ")                  #Enter a new password
        else:
            print("Username already exists.")
    elif action == "2":                                             #Modify a password
        username = input(f"To modify your password.\nenter your username: ")
        if username in accounts:                    #if the username is valid
            password = input("enter your old password : ")
            if password == accounts.get(username):
                password = input("enter a new password : ")
                accounts[username] = password
                print("password updated.")
            else:
                print("Wrong old password.")
        else:              #if the username is not in the dictionnary
            print(f"Invalid username. Please choose the action again.")
    elif action == "3":                                       #To remove an account
        username = input(f"To remove your account.\nenter your username: ")
        if username in accounts:                  #if the username is valid
            password = input("enter your password : ")
            if password == accounts[username]:                 #if the password is valid
                del accounts[username]
                print("account deleted.")
            else:
                password = input("Wrong password. Re-enter your password : ")
        else:
            print(f"Invalid username. Please choose the action again.")
    elif action == "4":
        for account in accounts:
            print(account)
    elif action == "5":
        break
    else:
        print("Incorrect input.")
print("Program existed.")
print(accounts)