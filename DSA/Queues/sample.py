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


