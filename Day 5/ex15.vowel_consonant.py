
vowels = "aeiou"
user_word = input("Please enter a word : ")
i = 0
for i in user_word:
    if i in vowels:
        print(f"{i.upper()} - vowel")
    else:
        print(f"{i.upper()} - consonant")