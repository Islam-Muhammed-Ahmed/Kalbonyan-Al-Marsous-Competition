# an input tells you to enter you name
name = input("Hi, what's your name? ")
# int is a method that accept integer number not string and it will get your age
age = int(input("How old are you? "))

# condition tells you if your age less than 13 years tells you are young to register
# else you are welcome to join
if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)    