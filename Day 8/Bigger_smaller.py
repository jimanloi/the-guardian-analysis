import random

def main():
    number_to_guess = random.randint(1,10)
    while True:
        guess = int(input("Enter a number between 0-10 :"))
        if guess != number_to_guess:
            if guess < number_to_guess:
                print("The number to guess is bigger.")
            elif guess > number_to_guess:
                print("The number to guess is smaller.")
        else:
            print("Bingo!")
            break

if __name__ == "__main__":
    main()