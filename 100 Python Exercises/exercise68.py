#Question:
'''
Create an English to Portuguese translation program. The program takes a word
from the user as input and translates it using the following dictionary as a
vocabulary source. In addition, return the message
"We couldn't find that word!" when the user enters a word that is not in the
dictionary. Also, make the program non case-sensitive meaning that for example,
both earth and Earth should return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva")

Hint 1: You should convert the string input to lowercase.

Hint 2: If you do dir(str)  you will see there's a lower  method there that
converts strings characters to lowercase.
'''
#Answer:
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translator(word):
    try:
        return d[word]
    except KeyError:
        return "We could not find that word!"

word_raw = input("Enter a word: ")
word = word.lower()
print(translator(word))
'''
