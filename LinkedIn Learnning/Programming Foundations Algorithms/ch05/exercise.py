# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i
    
    return None


print(find_item(87, items))
print(find_item(250, items))

# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx)// 2

        # if item is found, return the index
        if itemlist[midPt] == item:
            return midPt
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))

# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # using the all function
    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

    # using the brute force method
    for i in range(0, len(itemlist)-1):
        if (itemlist[i] > itemlist[i+1]):
            return False
    return True

print(is_sorted(items1))
print(is_sorted(items2))

