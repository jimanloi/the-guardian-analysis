import random

list_of_words = ["apple","banana","lemon","kiwi","mango","tomato","blueberry"]

word_to_guess = random.choice(list_of_words)
print(f"{word_to_guess}\n")
total_turns = len(word_to_guess) + 3
current_game = ["_"]*len(word_to_guess)
all_guessed_letter = []                                     #track all guessed letter in one game

for turn in range(total_turns):                             #Display turn information
    print(f"Turn {turn+1} of {total_turns}")
    print(f"word to guess :{' '.join(current_game)}")
    print(f"Previous guesses : {all_guessed_letter}\n")

    #user input
    guess_letter = input("Enter a letter: ").lower()
    if guess_letter.isalpha() == False or len(guess_letter) != 1:
        print(f"Invalid input.\n")
        continue
    if guess_letter.isalpha():
        all_guessed_letter.append(guess_letter)
        if all_guessed_letter.count(guess_letter) > 1:
            print("Letter used.\n")
            continue
        if guess_letter in word_to_guess:
            print("Correct.\n")
            for index, value in enumerate(word_to_guess):
                if guess_letter == value:
                    current_game[index] = guess_letter
        if guess_letter not in word_to_guess:
            print("Wrong guess.")
        if ''.join(current_game) == word_to_guess:
            break
if "_" in current_game:
    print(f"Failed. The word was : {word_to_guess}.")
else:
    print(f"Congratulations! The word is {word_to_guess}.\n")
