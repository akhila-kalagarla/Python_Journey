'''Queues - FIFO data structure
A queue is a linear data structure that follows the First In First Out (FIFO) principle.
It means the first element added to the queue is the first one to be removed. 
Queues are used in various applications such as task scheduling, resource management, and breadth-first search algorithms.
Queue operations include:
1. Enqueue: Add an element to the end of the queue.
2. Dequeue: Remove the front element from the queue.
3. Peek/Front: Retrieve the front element without removing it.
4. isEmpty: Check if the queue is empty.
5. Size: Get the number of elements in the queue.
Queues can be implemented using lists or linked lists in Python.
In Python, you can use a list to implement a queue, but it is not the most efficient way due to the O(n) time complexity of removing elements from the front of the list.
A more efficient way to implement a queue is by using the deque (double-ended queue) from the collections module, which provides O(1) time complexity for both enqueue and dequeue operations.
Here is an example of implementing a queue using list in Python:'''
# Using list to implement Queue
queue = []
# To add elements to the queue
queue.append('Naya sri')
queue.append('Rohini')
queue.append('Akhila')
queue.append('Kishor')
queue.append('Venkata Ramana')
print("Family of Kalagarla's:",queue)
# To remove elements from the queue
removed_element = queue.pop(0)
print("Removed element from the queue:",removed_element)
print(queue)
# To get the front element of the queue
front_element = queue[0]
print("Front element of the queue:",front_element)
# To check if the queue is empty
is_empty = len(queue) == 0
print("Is the queue empty?",is_empty)
# To get the size of the queue
size = len(queue)
print("Size of the queue:",size)



# Using class to implement Queue
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty!")
            return None
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty!")
            return None
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
# Sample usage
q = Queue()
q.enqueue('Naya sri')
q.enqueue('Rohini')
q.enqueue('Akhila')
q.enqueue('Kishor')
q.enqueue('Venkata Ramana')
print("Family of Kalagarla's:", q.items)
removed_element = q.dequeue()
print("Removed element from the queue:", removed_element)
print(q.items)
print("Front element of the queue:", q.front())
print("Is the queue empty?", q.is_empty())
print("Size of the queue:", q.size())


class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,data):
        self.q.append(data)
    def isEmpty(self):
        if len(self.q)==0:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.q.pop(0)
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            return self.q[0]
        
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.peek())