"""
V3 : "découper le programme en fonctions
au minimum 6 fonctions (mais sans doute +) :
load_accounts()
create_account()
change_password()
delete_account()
show_usernames()
save_accounts()
"""

accounts = {}

def load_accounts(filepath):
    with open(filepath, "r") as fp:
        for line in fp:
            username, password = line.strip().split(": ")
            accounts[username] = password
        return accounts

def create_account(accounts):
    username = input(f"To create an account.\nusername : ")  # Enter a new username
    if username not in accounts:
        accounts.setdefault(username)  # Create a new user
        accounts[username] = input("password : ")  # Enter a new password
        print("account created.")
    else:
        print("Username already exists.")

"""def check_username_password():
    if password == accounts.get(username):
        return True
    return False"""

def change_password():
    print("To modify your password")
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    if password == accounts.get(username):
        password = input("enter a new password : ")
        accounts[username] = password
        print("Password updated.")
    else:
        print("Wrong input")

def delete_account():
    username = input("Enter your username : ")
    password = input("Enter your old password : ")
    if password == accounts.get(username):
        del accounts[username]
        print("account deleted.")
    else:
        print("Wrong input")

def show_usernames():
    for account in accounts:
        print(account)

def save_accounts():
    with open("accounts.txt", "w") as fp:
        for username, password in accounts.items():
            fp.write(f"{username}: {password}\n")


# Programme principal
def main():
    accounts = load_accounts("accounts.txt")
    while True:
        choice = input("What do you want to do ? : ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            change_password()
        elif choice == "3":
            delete_account()
        elif choice == "4":
            show_usernames()
        elif choice == "5":
            save_accounts()
            break
        else:
            print("Incorrect input.")
    print("Program exited.")

if __name__ == "__main__":
    main()
