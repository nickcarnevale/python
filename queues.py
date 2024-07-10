# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

# Big O
# ------------
# append()              O(1)
# appendleft()          O(1)
# pop()                 O(1)
# popleft()             O(1)
# len(dequeue)          O(1)
# dequeue[0]            O(1)
# dequeue[-1]           O(1)

# index()               O(n)
# insert(i, item)       O(n)
# remove                O(n)
# count                 O(n)
# reverse               O(n)
