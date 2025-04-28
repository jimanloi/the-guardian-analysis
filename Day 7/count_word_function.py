#definir une fonction qui compte le nombre de mots
#d'un string et renvoie ce nombre

def count_words(sentence):
    number_of_word = len(sentence.split())
    return number_of_word

sentence = "  Hello  how are you "
print(count_words(sentence))


