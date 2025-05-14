# Like a stack, the queue is a linear data
# structure that stores items in a First In
# First Out (FIFO) manner. With a queue, the
# least recently added item is removed first.

# Enqueue: Adds an item to the queue. If the
# queue is full, then it is said to be an
# Overflow condition – Time Complexity : O(1)
# Dequeue: Removes an item from the queue. The
# items are popped in the same order in which
# they are pushed. If the queue is empty, then
# it is said to be an Underflow condition – Time Complexity : O(1)
# Front: Get the front item from queue – Time Complexity : O(1)
# Rear: Get the last item from queue – Time Complexity : O(1)


from collections import deque
# Creates an empty deque object and assigns it to variable q.
q = deque()
# Adds a
q.append('a')
# Adds b
q.append('b')
# Adds c. Now its deque(['a', 'b', 'c'])
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
# Removes and prints the first element from the queue ('a').
# Queue becomes: deque(['b', 'c'])
print(q.popleft())
print(q.popleft())
# Removes and prints the last remaining element ('c').
# Queue becomes: deque([]) (now empty)
print(q.popleft())

print("\nQueue after removing elements")
print(q)

