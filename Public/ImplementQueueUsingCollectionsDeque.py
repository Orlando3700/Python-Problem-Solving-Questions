# Write a Python code to implement a queue using collections.deque

# This imports the deque class from Python’s built-in collections module.
# deque is like a list but optimized for fast
# appending and popping from both the front
# and back
from collections import deque

class Queue:
    def __init__(self):
        # self.queue = deque() creates an empty
        # deque and stores it in the instance
        # variable self.queue.
        self.queue = deque()

    # Defines a method enqueue to add an item to
    # the end of the queue.
    # self.queue.append(item) adds the item to
    # the right end of the deque.
    def enqueue(self, item):
        self.queue.append(item)

    # Defines a method dequeue to remove and
    # return the front item of the queue.
    # self.queue.popleft() removes the item from
    # the left end (front) of the deque.
    # if self.queue checks if the queue is not
    # empty. If it is empty, it returns None
    # instead of throwing an error.
    def dequeue(self):
        return self.queue.popleft() if self.queue else None

# Creates a new instance of the Queue class and assigns it to variable q.
q = Queue()
# Adds 1 to queue
q.enqueue(1)
# Adds 2 to queue, now queue contains [1, 2]
q.enqueue(2)
# Removes and prints the first item (1) from the queue
print(q.dequeue())  # 1

