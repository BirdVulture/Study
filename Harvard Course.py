#https://www.youtube.com/watch?v=nLRL_NcnK-4&t=52792s


#Documentation
#https://docs.python.org/3.12/library/index.html
  
#STR
# Ask user for their name
'''name = input("What is your name?")

#remove whitespace from str
name = name.strip()

#Capitalize name 
name = name.capitalize()

#Title
name = name.title()

#Split user's name into  first name and last name (to split strings by separator)
first, last = name.split(" ")
 
print(f"Hello, {name}")

print(first,"\n" ,last, sep= "--", end= "\n")

print(first + last)'''

#INTEGER 1:04
'''
x = int(input("What's x? "))
y = int(input("What's y?"))

z = x + y

print(z)
'''
#FLOAT 1:19
'''
x = float(input("What's x? "))
y = float(input("What's y?"))

z = x + y

print(z)
 
#round (округление)

z = round(x + y)

z = round(x / y, 2) #round

print(z)

'''
#FUNCTIONS (def) 1:31
'''
def hello(to):
    print("hello, ", to)  
    

hello()


def main():
    hello()
    name = input("What is your name? ")
    hello(name)


def mainTwo():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n): #степнь n ** 2
    return pow(n, 2)
'''

# Conditionals (условия) 1:50
'''
xy = int(input("What's x? "))
 = int(input("What's y?"))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal than y")


if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal than y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal than y")   
'''
    
'''
score = int(input("Score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: D")

# This code is better
if 90 <= score <=100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: D")

# This code is more better
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: D")
'''
# Parity
'''
x = int(input("What's x? "))
y = int(input("What's y?"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


# Even or odd (четное/нечетное) 
def is_even(n):
    if n % 2 ==0:
#        return True
#    else:
#        return False


# the better code
        
          
def is_even_two(n):
    return True if n % 2 == 0 else False



# The more better code
def is_even(n):
    return n % 2 == 0
'''    

#match
'''
name = input("What's your name? ")

if name == "Harry":
    print("Griffindor")
elif name == "Hermione":
    print("Griffindor")
elif name == "Ron":
    print("Griffendor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who")
'''
# Another way (Соответствие)
'''
match name:
    case "Harry":
        print("Griffendor")
    case "Hermione":
        print("Griffendor")
    case "Ron":
        print("Griffenor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# the better code 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffendor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

'''
#Loops 2:46
'''        
i = 3

while i != 0: # while  i is not equal 0 
    print("meow")
    i = i - 1
'''
'''
for i  in [0, 1, 2]:
    print("meow")

#the better code
for i in range(3):
    print("meow")

#the more better code
print("meow\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break 
'''
'''
#the better code (через функции)

def main():
    number = get_number()
    meow(number)

while True:
    n = int(input("What's n? "))
    if n > 0:
        break 

for i in range(n):
    print("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
        return n

def meow(n):
    for _ in range(n):
        print("meow")



main()
'''

# list 3:21
'''
students = ["Hermione", "Harry", "Ron"]
'''
 
#for each element in list
''' 
for student in students:
    print(student)
'''

'''
for i  in  range(len(students)):
    print(i + 1, students[i])
'''
    



# dicts 3:32
'''
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Griffindor", "Griffindor", "Griffindor", "Slytherin"]
'''
'''
students = {
    "Hermione": "Griffidor",
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"
}


print(students["Hermione"])
print(students["Harry"])
print(students["ron"])
print(students["Draco"])


for student in students:
    print(student, students[student], sep= ", ")
'''
'''
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
'''
'''
def main():
    print_column(3)
'''
'''
def print_column(height):
    for _ in range(height):
        print("#")
'''
# more clever code
'''
def print_column(height):
    print("#\n" * height, end="")

def print_row(width):
     print("?" * width)

def print_square(size):

    #for each row in square 
    for i in range(size):

        #for efch brich in row
        for j in range(size):

            #print brick
            print("#", end="")

        print()     
'''
#another way
'''
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(widht):
    print("#" * widht)

main()
'''

#Exceptions 4:15 (обработка ошибок ( если введен неверный тип данных))
'''
def main():
    x = get_int()
    print(f" x i {x}")


def get_int():
    while True: #запрашивать x пока ч не станет равно int
        try:
            x = int(input("What's x?"))       
            print(f"x is {x}")

        except ValueError:
            print("x is not an integer")

        else:
            return x


# the better code
        
def get_int():
    while True: #запрашивать x пока ч не станет равно int
        try:
           return int(input("What's x?"))       
           
        except ValueError:
            print("x is not an integer")

#another way without  error message
            
def get_int(prompt):
    while True: #запрашивать x пока ч не станет равно int
        try:
           return int(input(prompt))       
           
        except ValueError:
            pass #цикл без сообщеия об ошибке 


main()
'''
#Libraries 4.54
#module random
'''
import random

coin = random.choice(["heads", "tails"])


from random import choice

coin = choice(["heads", "tails"]) 
print(coin)

number = random.randint(1, 10)
print (number)

cards = ["jack", "queen", "king"]
random.shuffle(cards) #перемешать порядок элементов из списка
for card in cards:
    print(card)




#statistics
    
import statistics

print(statistics.mean([100, 90]))


#5.13 module sys

import sys

print("hello, my name is ", sys.argv[0]) #from filename

try: 
    print("hello, my name is ", sys.argv[0])

except IndexError:
    print("hello, my name is ", sys.argv[0])

#

if len(sys.argv) < 2:

    print("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments")

else:
     print("hello, my name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

else:
    print("hello, my name is ", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is ", arg)


#Slices 5:32

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)  

#PIP - package manager pypi.org
#python3 -m pip install "module name"
'''

#APIes pypi.org 5:47

#JSON 5:48
'''
import json
import requests
import sys

#if len(sys.argv) != 2:
#    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + "weezer")

#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
'''
# Libraries 6:02 
#Export and import functions from another file

#sayngs.py file with functions
'''
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

main()
'''
#another file
'''
import sys

from sayings import goodbye

if len((sys.argv)) == 2:
    goodbye(sys.argv[1])
'''
    
#Unit Tests 6:09

#program Calculator
'''
def main ():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

if __name__ == "__main__":
    main()
# test program
    

def main():
    test_square()

from calculator import square

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squred was not 9")


if __name__ == "__main__":
    main()
'''
#assert 6:20
'''
def main():
    test_square()

from calculator import square

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")    


if __name__ == "__main__":
    main()
'''
#pytest 6:25

# pip3 inastall pytest
'''
from calculator import square
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
'''
# run pytest!!!
'''
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
'''
#program
'''
def main():
    name = input("What's your name?")
    hello(name)

def hello(to="world"):
    print("hello,", to)

if __name__ == "__name__":
    main()
'''
# test program
'''
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"

def test_argument2():
    for name in ["Hermione", "Harry"]:
        assert hello(name) == f"hello, {name}"

#packages
'''

#File I/O 7:00 
#LIST
'''
names = []

for _ in range(3):
    name = input("What's your name?")
    names.append(name)


print(f"hello, {name}")

#clever code

names = []

for _ in range(3):
    names.append(input("What's your name?"))


print(f"hello, {name}")
'''
#create file
'''
name = input("What's your name?")

file = open("names.txt", "w")
file.write(name)
file.close()

#clever code
name = input("What's your name?")

file = open("names.txt", "w")
file.write(f"{name}\n")
file.close()

#with
# add data to file
name = input("What's your name?")

with open("names.txt", "a") as file: # "a" - add data to file
    file.write(f"{name}\n") # add data to new line in file

#read lines from file and write it to list

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip()) #rstrip remove white spaces

#more compact code

with open("names.txt", "r") as file:
    for line in file:
        print("hello, ", line.rstrip())

names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

#more compact code

with open("names.txt", "r") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip()) 
'''

#csv file
# Export from .csv, split each line for two elements by ,
'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")


students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''

#Dictionaries! key-value

'''
students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


#sort dictionaries
    
students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


#with lambda function

students = []
with open ("students.csv") as file:
    for line in file:
        name, house =line.rstrip().split(",")
        student = {}
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student[name]):
    print(f"{student['name']} is in {student['house']}")


#csv library
    
import csv

students = []
with open ("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


#back the dictionary 

import csv

students = []
with open ("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

#8:14

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

#

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


#Images
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
'''

# REGULAR EXPRESSIONS 8:30

'''
email = input("What's your email?").strip()


if "@" in email and "." in   email: 
    print("Valid")
else:
    print("Invalid")

username, domain = email.split("@") 

#if username and ". " in domain: #var 1

if username and domain.endswith(".edu"): #var 2    
    print("valid")
else:
    print("Invalid")
'''

#re - library for regular expressions

import re
'''
email = input("What's your email?").strip()
#if re.search(r".+@.+\.edu", email):
#if re.search(r".+@.+\.edu", email):
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#if re.search(r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_\.]+\.edu$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov)$", email):   

    print("Valid")
else:
    print("Invalid")

'''
'''
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last} "
print(f"hello, {name}")

import re
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last = matches.groups(1)
    first = matches.group(2)
    name = f"{first} {last}"

#another way
if matches:
    name = matches.group(2) +" " + matches.group(1)
    
print(f"hello, {name}")

#twitter https://twitter.com/davidjmalan username from url
import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/", "")
#username = url.replaceprefix("https://twitter.com/")
#username = re.sub(r"^(https?://)?(www\.|)?twitter\.com/", "", url)
#print(f"Userneme: {username}")


matches = re.search(r"^https?://(www.\.)?twitter\.com/.+$", url, re.IGNORECASE)

if matches:
    print(f"username:", matches.group(2))


if matches := re.search(r"^https?://(?www.\.)?twitter\.com/.([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"username:", matches.group(2))
'''
# OBJECT ORIENTED PROGRAMMING 10:35
#file student.py

'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
'''

def main():  
    name, house = get_student()
    
def get_name():
    name = input("Name: ")
    return name

def get_house():
    return input("House: ")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()

#tuple 10:48 кортеж

    

#OOP OBJECT-ORIENTED PROGRAMMING 10:38
#student.py
'''
# List and tuple
def main():
    name = get_name()
    house = get_house()
    name, house = get_student()
    student = get_student()
    if student[0] == "Padma": #изменение значения в списке в зависимости от значения ключа
        student[1] = "Ravenclaw"

    print(f"{name} from {house}")
    print(f"{student[0]} from {student[1]}")

def get_name():
    name = input("Name: ")
    return name


def get_house():
    return input("House: ") 
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
    

if __name__ == "__main__":
    main()

#Dictionary
def main():
    student = get_student()
    if student[0] == "Padma": #изменение значения в словаре в зависимости от значения ключа
        student[1] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

#CLASSES

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() # creation object student from class Student
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student
'''
#Creating objects from classes 11:10
#attributes is a instance variables 11:13

#methods 11:17
'''
class Student:
    def __init__(self, name, house): #initialization attributes in class
        self.name = name
        self.house = house


class Student_two:
    def __init__(self, name, house, patronus): #initialization attributes in class
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid  house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self): #function for transform object to string
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "1"
            case "Otter":
                return "2"
            case _:
                return "3"


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)
    print(student.charm())

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus) #Constructor
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except Value:
        Value = 1



#inncpsuliation 11:28

#raiese (for exceptions)

class Student:
    def __init__(self, name, house): #initialization attributes in class
        self.name = name
        self.house = house

#__init__
class Student_two:
    def __init__(self, name, house, ): #initialization of attributes and validation values in class
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid  house") #raise exception
        self.name = name
        self.house = house
        
#__str__  
    def __str__(self): #function for transform object to string
        return f"{self.name} from {self.house}"
    


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)
  

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

def get_student_two():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except Value:
        Value = 1


#properties 12:00 decorators

class Student_two:
    def __init__(self, name, house, ): #initialization attributes in class
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid  house")
        self.name = name
        self.house = house
        

    def __str__(self): #function for transform object to string
        return f"{self.name} from {self.house}"
    
    #Getter
    @property
    def house(self):
        return self._house
    
    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()

    print(student)


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

'''

#classmethod 12:29
''' 
import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    
    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)


hat = Hat()
hat.sort("Harry")

#classmethod



class Hat:
   
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


hat = Hat()
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    
    def sort(self, name):
        house = random.choice(self.houses)
        print(name, "is in", house)



Hat.sort("Harry")

#####

class Student:
    def __init__(self, name, house): #initialization attributes in class
        self.name = name
        self.house = house

    def __str__(self): #function for transform object to string
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)

'''

#Inheritance 12:57
'''
class Wizard:
    def __init__(self, name): 
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence")

#operator overloading 13:12
#Vault

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"  

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts) 

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)



total = potter + weasley

print(total)

#set 13:30

students = [
    {"name": "Hernione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

houses = [] #unic houses 1
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

houses = set() #unic houses set
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

'''

#GLOBAL VARIABLES

balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

    def main():
        account = Account()
        print("Balance: ", account.balance )
        account.deposit(100)
        account.withdraw(50)
        print("Balance: ", account.balance)

if __name__ == "__main__":
    main()

#constants

MEOWS = 3 #constant

for _ in range(MEOWS):
    print("meow")


###

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()


#type hints start program with mypy  
#pip3 install mypy

def meow(n: int) -> None:
    for _ in range(n):
        print(meow)

def meow(n: int) -> str:
        return "meow\n" * n #multipication of strings
 

number: int = int(input("Nunber: "))

meow(number)


#docstrings # - documentation

def meow(n: int) -> str:
        
        return "meow\n" * n #multipication of strings
 

number: int = int(input("Nunber: "))

meow(number)

#use command line arguments 14:23

import sys

if len(sys.srgv) ==1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print(meow)
else:
    print("usage: meows.py")


#argparse analizis command line arguments

import argparse

parser = argparse.ArgumentParser(deskription="Meow like a cat")

parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

#unpacking 14:39

first, last = input("What's your name? ").split(" ")

print(f"helo, {first}")


def total(galleons, sickles, knuts):
    return (galleons * 17 +sickles) *29 + knuts

coins = [100, 50, 25]
#list
print(total(coins[0], coins[1], coins[2]), "Knuts")
#unpack list
print(total(*coins), "Knuts") # * - for unpack list to multiple values

#dictionary

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

#unpack dictionary
print(total(**coins), "Knuts")


#### unpack all elements
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)


### 15:00 for diagnostic
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles= 50, knuts=25)


#map

...

#list comprehensions

students = [
    {"name": "Hernione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

griffindors = [
    student["name"] for student in students if student["house" == "Gryffindor"]
]

for gryffindor in sorted(griffindors):
    print(gryffindor)

#filter 15:21

students = [
    {"name": "Hernione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(griffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])

#dictionary comprehensions 15:28

students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name:": student, "house": "Gryffindor"})

###
gryffindors = [{"name:": student, "house": "Gryffindor"} for student in students]

### ictionary comprehensions

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

#enumerate
...

#generators 15:37

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n): # iterator function returns litlle bit of data, not all of data at a time
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()

