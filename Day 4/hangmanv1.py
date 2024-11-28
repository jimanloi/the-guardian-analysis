

word_to_guess = "cat"
good_answer = ["_"] * len(word_to_guess)
number_trial = 10

while "_" in good_answer and number_trial > 0:                         #while the word is not found and the user can still play                                                      #the first trial
    guess_letter = input(f"{good_answer} Type a letter to guess the word : ")
    if guess_letter in word_to_guess :                                            #if the letter is correct
        good_answer[word_to_guess.index(guess_letter)] = guess_letter              #change the "_" on the list to the letter
        print(f"Correct.")
        if good_answer == list(word_to_guess):
            print(f"Congratulations! The word is {word_to_guess}.")
    else:                                                                       #if the letter is wrong
        number_trial -= 1
        print(f"Wrong. You have {number_trial} lives left.")
if "_" in good_answer and number_trial == 0:                        #if the word is not found and the player cannot play anymore
        print("Game over.")

