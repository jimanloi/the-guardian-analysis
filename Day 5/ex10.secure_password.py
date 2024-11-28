"""Your script must check the complexity of the user password:

    A password length equal to 0 means the user didn't enter a password.
    A password with less than 6 characters is considered as too weak.
    A password with at least 6 characters is considered as valid.
    A password with 8 or more characters is considered as strong.
"""

user_password = input("Enter your password : ")
password_length = len(user_password)
if password_length == 0:
    print("invalid")
elif password_length < 6:
    print("too weak")
elif password_length >= 8:
    print("strong")
elif password_length >= 6:
    print("valid")
