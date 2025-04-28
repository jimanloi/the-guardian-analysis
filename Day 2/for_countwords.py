#message = "Hello World!"
#for character in message:
   # print(character)
from itertools import count

#Exercise FOR - count words

#Method 1
sentence = "How"
counter = 0
for letter in sentence:
    if letter == " ":   #in the case where we don't have extra space
        counter += 1
if len(sentence) != 0:
    counter += 1
print("Number of words:",counter)

#Method 2
number_words = len(sentence.split())
print("Number of words:", number_words)
