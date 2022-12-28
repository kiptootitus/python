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



def my_function(*kids):
    print("The youngest child is " + kids[0])

my_function(input("Enter your name: "), input("Enter your name: "), input("Enter your name: "))

