def day_of_week(day):
    switcher = {
        0: "Sunday",
       1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(day, "Invalid day of week")

print(day_of_week(1))
print(day_of_week(6))
print(day_of_week(42))
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# RegEX 
import re
string = "Hello my name is Titus. I am 10 years old. Titus will be having 11th birthday on 10th of October at spain palace."

p = re.findall(r"\Bain", string)
if p:
    print("There is a match in the string")
else:
    print("No match")

o ="My name is Titus. I am a 3rd year student at Karatina University. My github username is @titus254"
c=re.search("^My",o)
if c: 
    print("There is a match in the string")
else:
    print("No match")
import re

str = 'an example word:Titus'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
  
mlist = ["apple", "banana", "cherry"]
for x in mlist:
  print(x)

# class myNumbers:
#     def __iter__self (self):
#         self.a = 1
#         return self
    
#     def __next__self(self):
#         x = self.a
#         self.a += 1
#         return x
        
# myclass = myNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))                      



# def my_function(*kids):
#     print("The youngest child is " + kids[0])

# my_function(input("Enter your name: "), input("Enter your name: "), input("Enter your name: "))

# decorators

def say_hello(name):
    return f"Hello, {name}!"

def shout(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

# Add the shout decorator to the say_hello function
say_hello = shout(say_hello)

print(say_hello("Alice"))  # prints "HELLO, ALICE!"

@shout 
def say_hi(name):
    return f"Hi, {name}!"

print(say_hi("Alice"))  # prints "HI, ALICE!"


def say_Name(city):
 return f"Welcome, {city}!"

def tell(func):
    def wrapper(city):
        return func(city).lower()
    return wrapper
say_Name = tell(say_Name)


print(say_Name("Nairobi"))


@tell
def say_Country(country):
    return f"Welcome, {country}!"

print(say_Country("Kenya"))

     
# lambda functions
str1 ="Hello, My name is Titus"
str2 ="Hello, My name is Nomad"
str3 ="Hello, My name is Meshack"
str3 ="Hello, My name is Kering"
str4 ="Hello, My name is Faith"
# lambda function
re_upper = lambda str4: str4.upper()
print(re_upper(str4))


# lambda function with list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# to multiply each number by 2
result = list(map(lambda x: x * 2, numbers))
print(result)


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final = list(filter(lambda x: (x % 2 != 0), li))
print(final)



class cars:    
    def __init__(self, name, color, model, price):
        self.name = name
        self.color = color
        self.model = model
        self.price = price
    
    def __str__(self):
        return f"{self.name} is {self.color} and it costs is {self.price}" 
car = {("Toyota", "Black", "2019", "100,000Ksh"), ("BMW", "White", "2018", "200,000Ksh"), ("Mercedes", "Red", "2017", "300,000Ksh"), ("Audi", "Blue", "2016", "400,000Ksh")}

above = list(filter(lambda x: (x[3] > "200,000Ksh"), car))
print(above)


# maximum number in a list
import functools

# list of numbers
lis = [ 1 , 3, 5, 6, 2, ]

print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

# In Python, an iterator is an object that can be used to iterate over the elements of a sequence (such as a list, tuple, or string). Iterators are implemented using two methods: __iter__() and __next__().
# Define a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get an iterator for the list
iter_obj = iter(numbers)

# Use the iterator to iterate over the list
while True:
    try:
        # Get the next element from the iterator
        element = next(iter_obj)
        print(element)
    except StopIteration:
        # If there are no more elements, exit the loop
        break
