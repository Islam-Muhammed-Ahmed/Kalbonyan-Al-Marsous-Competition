from ast import While
from operator import le


countries = [
    "Egy",
    "Ksa",
    "Yem",
    "Lib",
]

for country in countries:
    print(country, "is an Arab country")
    
print("##################")
    
x = 1
while x <= 50:
    print(x)
    # x = x + 1
    x += 1
print("count to 50 end")

print("##############")

# solve Challenge using while an for loop
fruits = [
    'apples',
    'bananas',
    'dragon fruit',
    'mangos',
    'nectarines',
    'pears',
]
# print('Our fruit selection:')
# for fruit in fruits:
#     print(fruit)


print('Our fruit selection:')
f = 0 
# using range method to fix  index error
# using in 'cause <= giving Exception has occurred: TypeError '<=' not supported between instances of 'int' and 'range'
while f in range(len(fruits)) :
    print("i love ", fruits[f])
    f = f + 1
