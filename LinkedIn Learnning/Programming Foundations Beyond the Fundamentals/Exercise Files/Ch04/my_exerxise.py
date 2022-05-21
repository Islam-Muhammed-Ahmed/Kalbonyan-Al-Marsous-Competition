# concat strings

value = input("enter your favorite month: ")
print(value + " is my favorite month")

# concat strings with nums
val = input("Enter a num: ")
print(val + "this is the number you Entered")
print("when you divide it by 5, this is your result: ")
#  why we use int() func ? we use it to convert number entry to a number 

print(int(val) / 5)

# some string methods 
f_name = "islam"
l_name = "muhammed"
# capitalize strings
print(f_name.capitalize())
print(l_name.capitalize())

# lower case
print(f_name.lower())
print(l_name.lower())

# upper case
print(f_name.upper())
print(l_name.upper())
# some of them find() index() splice()

# regular expression
from pickletools import float8
import re

phone_number = "0102-7247-203"
bank_acc = "12121-12323-2585-22"
# r = means that the string we are gonna type it may contains back slashes that the compiler should ignore it.

four_digits_expression = r"\d{4}"

print(re.search(four_digits_expression, phone_number))
print(re.search(four_digits_expression, bank_acc))

# challenge solve
# make the user enter the distance he walked in miles and convert it into km
miles = input('Enter a distance in miles: ')

# kilometers_value = miles_value * 1.609344

miles_value = int(miles)
# instructor ans he used float() to convert it to num

kilometers_value = miles_value * 1.609344

# her i use round method to get rid off the floating numbers this method if the float num < .5 it will ignore them and if it's > .5 it will add to result 1 and ignore the float nums

print(round(kilometers_value), "Km")
