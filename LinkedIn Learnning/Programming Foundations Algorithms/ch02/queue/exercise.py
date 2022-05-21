# ****note****=> we can use a regular list as queue in python but it's very incefficient to do so 
# and that's 'cause removing item from the front of a list  a big O of linear time complexity 
# 'cause items will need to shifted down their slots.
# ###################

# try out the Python queue functions
from collections import deque

# create a new empty deque object that will function as a queue
queue = deque()

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
