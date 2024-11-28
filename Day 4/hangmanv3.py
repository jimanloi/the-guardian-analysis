word_to_guess = "banana"
good_answer = ["_"] * len(word_to_guess)
all_answer = []
number_trial = 10
while "_" in good_answer and number_trial > 0:                                  #while the word is not found and the user can still play                                                      #the first trial
    guess_letter = input(f"{good_answer} Type a letter to guess the word : ")
    all_answer.append(guess_letter)                                              #record all input
    if all_answer.count(guess_letter) > 1:                                      #Check if the input has been used before
        print("The letter has already been used. Try again.")                       #If yes; type again
    if all_answer.count(guess_letter) == 1:                                        #if no,continue
        if guess_letter in word_to_guess :                                            #if the letter is correct
            for index, value in enumerate(word_to_guess):
                if guess_letter == value:
                    good_answer[index] = guess_letter
            if good_answer == list(word_to_guess):
                print(f"Congratulations! The word is {word_to_guess}.")
        else:                                                                       #if the letter is wrong
            number_trial -= 1
            print(f"Wrong. You have {number_trial} lives left.")
if "_" in good_answer and number_trial == 0:                        #if the word is not found and the player cannot play anymore
        print("Game over.")