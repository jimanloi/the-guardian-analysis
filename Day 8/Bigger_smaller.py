def main():
    number_to_guess = 5
    guess = int(input("Enter a number between 0-10 :"))
    if guess != number_to_guess:
        if guess < number_to_guess:
            print("The number to guess is bigger.")
        elif guess > number_to_guess:
            print("The number to guess is smaller.")
    else:
        print("Bingo!")

if __name__ == "__main__":
    main()