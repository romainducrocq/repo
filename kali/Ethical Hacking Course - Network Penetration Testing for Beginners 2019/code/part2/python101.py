#!/bin/python3

#print string
print("Strings and things:")
print('Hello, world!')
print("""Hello, this is a multi-
line string!""")
print("This is" + " a concat")
print("\n") #new line

#Maths
print("Math time:")
print(50 + 50) #add
print(50 - 50) #substract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponent
print(50 % 6) # modulo
print(50 // 6) #no leftover
print("\n") #new line

#Variables and methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #first letter capitalize

name = "Romain"
age = 23 #int int(23)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(23.9)) #does not round

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)
print("\n") #new line

#Functions
print("Now, some functions:")

def who_am_i():
    name1 = "Romain"
    age = 23
    print("My name is " + name1 + " and I am " + str(age) + " years old.")

who_am_i()
#print(name1) #name1 is local to the function

#adding in parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

#adding multiple parameters
def add(x, y):
    print(x + y)

add(7, 7)
add(304, 207)

#return
def multiply(x, y):
    return x * y

print(multiply(7, 7))

def square_root(x):
    return x ** .5

print(square_root(64))

def new_line():
    print("\n")

new_line()

#Boolean expressions
print("Boolean expressions")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and, test_or, test_not)

new_line()

#Conditional statements
print("Conditional statements:")
def soda(money):
    if money >= 2:
        return "You've got yourself a soda!"
    else:
        return "No soda for you!"

print(soda(1))
print(soda(2))
print(soda(3))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting tipsy!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif(age < 21) and (money >= 5):
        return "Nice try, kid."
    else:
        return "You're too poor and too young."

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 5))
print(alcohol(20, 4))

new_line()

#Lists
print("Lists have brackets:")
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(1)
print(movies)

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah", "Jeff"]
combined = zip(movies, person)
print(list(combined))

movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]
person = ["Heath", "Jake", "Leah"]
combined = zip(movies, person)
print(list(combined))

new_line()

#Tuples
print("Tuples have parentheses and cannot change:")
grades = ("A", "B", "C", "D", "F")
print(grades[1])

new_line()

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage"]

for x in vegetables:
    print(x)

new_line()

print("While loops - execute as long as True:")

i = 0
while i < 10:
    print(i)
    i += 1
