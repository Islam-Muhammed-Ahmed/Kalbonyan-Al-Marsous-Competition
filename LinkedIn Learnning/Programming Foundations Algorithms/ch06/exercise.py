# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
            "orange", "apple", "pear", "banana", "orange",
            "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable to perform a filter
filter = dict()

# loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)

# using a hashtable to count individual items

# define a set of items that we want to count
# items = ["apple", "pear", "orange", "banana", "apple",
#          "orange", "apple", "pear", "banana", "orange",
#          "apple", "kiwi", "pear", "apple", "orange"]

# create a hashtable object to hold the items and counts
counter = dict()

# iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
print(counter)

# use a recursive algorithm to find a maximum value


# declare a list of values to operate on
itemsNum = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(itemsNum):
    # breaking condition: last item in list? return it
    if len(itemsNum) == 1:
        return itemsNum[0]

    # otherwise get the first item and call function
    # again to operate on the rest of the list
    op1 = itemsNum[0]
    print(op1)
    op2 = find_max(itemsNum[1:])
    print(op1, op2)

    # perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2


# test the function
print(find_max(itemsNum))
