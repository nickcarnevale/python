# Test: Define a class and in that class init hash maps, loops queues, 

from collections import deque
import heapq

class oop:

    def __init__(self, num):
        self.num = num
        self.hmap = {}
        self.queue = []
        self.heapArray = []

    def get_num (self):
        return self.num
    
    def set_num(self, num):
        self.num = num


    def initalize_map(self, arr):
        for i, n in enumerate(arr):
            self.hmap[n] = i
        print(self.hmap)
        print(2 in self.hmap)

    def init_queue(self, arr):
        queue = deque() 
        for i in range(len(arr)):
            queue.append(arr[i])
        print(queue)
        queue.popleft()
        queue.pop()
        print(queue)
        queue.appendleft(1)
        print(queue)

    def init_heap(self, arr):
        heapq.heapify(arr)
        print(heapq.heappop())

        heapq.heappush(arr, 1)

        print(arr)
    

    