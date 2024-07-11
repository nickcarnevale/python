# Heaps
# Used to find the min and max of a set of values frequently O(1)

# Initalization
# Start with an empty list
# BY DEFAULT HEAPS IN PYTHON ARE MIN HEAPS
import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min value is always at index 0
print(minHeap[0])

# To iterate through a min heap from smallest to largest
while len(minHeap): # will repeat till non-zero
    print(heapq.heappop(minHeap))


# MAX HEAPS
# work around, multiple everything by -1

maxHeap = []
#insert values in as negatives
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -4)
heapq.heappush(maxHeap, -5)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max value is always at index 0 multiplied by -1
print(-1 * maxHeap[0])

# to print mult by -1
while len(maxHeap): # will repeat till non-zero
    print(-1 * heapq.heappop(maxHeap))


# If you already have the array of values:
# Call heapify()   O(n)

arr = [5,2,34,5,7,4,2,8]
heapq.heapify(arr)

while arr: # while array is non-empty
    print(heapq.heappop(arr))
    if(len(arr)==1):
        break



# Big O
# ------------
# heappush()        O(log n)
# heappop()         O(log n) 

# heapify()         O(n)