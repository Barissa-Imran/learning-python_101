#  Write a Python program that accepts a string and calculates the number of digits and letters.

# Sample Data: Python 3.2

string = "Python 3.2"

letters = 0
digits = 0

for i in string:
    if i.isnumeric():
        digits += 1
    elif i.isalpha():
        letters += 1
        
print("Letters: {}".format(letters))
print("Digits: {}".format(digits))



