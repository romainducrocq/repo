#!/bin/python3

#Importing
print("Importing is important:")
import sys #system functions and parameters

from datetime import datetime
print(datetime.now())

from datetime import datetime as dt
print(dt.now())

def new_line():
    print("\n")

new_line()

#Advanced strings
print("Advanced strings:")
my_name =  "Romain"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word
print(sentence.split()[-1]) #split default delimiter is " "

sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print(sentence_join)
print("\n".join(sentence_split))

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter in word)
print(letter in word.lower()) #Imporved - case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "                           hello                        "
print(too_much_space.strip()) #strip default delimiter is " "

full_name = "omain Ducrocq"
print(full_name.replace("omain", "Romain"))
print(full_name.find("Ducrocq"))

#Placeholders
movie = "The Hangover"
print("My favourite movie is {}.".format(movie))

def favourite_book(title, author):
    return "My favourite book is \"{}\", which is written by {}".format(title, author)

print(favourite_book("GOT", "GRRM"))

new_line()

#Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipples": 6} #drink is key, price is values
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees["Legal"] = ["Mr. Frond"] #add new key: value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks["White Russians"] = 8
print(drinks)

print(drinks.get("White Russians"))
print(drinks.get("Vodka Coca"))

for d in drinks:
    print(d)

print(drinks["White Russians"])

#List and disctionaries
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Bob", "Leah", "Jeff"]
combined = zip(movies, person)
movie_dictionnary = {key: value for key, value in combined}
print(movie_dictionnary)
