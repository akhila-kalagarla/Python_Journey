'''Stack - A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
It means the last element added to the stack is the first one to be removed. 
Stacks are used in various applications such as function call management, expression evaluation, and backtracking algorithms.
Stack operations include:

1. Push: Add an element to the top of the stack.
2. Pop: Remove the top element from the stack.
3. Peek: Retrieve the top element without removing it.
4. isEmpty: Check if the stack is empty.
5. Size: Get the number of elements in the stack.
Stack can be implemented using lists or linked lists in Python.
In Python, you can use a list to implement a stack, as it provides built-in methods like append() for push and pop() for pop operations.

Overflow and underflow conditions can be handled by checking the size of the stack before performing push or pop operations.
Overflow occurs when trying to push an element onto a full stack. 
Underflow occurs when trying to pop an element from an empty stack.

# Implementation of stack 
using Array (list) in Python
using linked list in Python - Deque from collections, LIFO Queue
'''


# To create a stack using list
stack = []
#To add elements to the stack
stack.append('Venkata Ramana')
stack.append('Rohini')
stack.append('Akhila')
stack.append('Kishor')
stack.append('Naya sri')
print("Family of Kalagarla's:",stack)
#To print peek element from the stack
topelement = stack[-1]
print("Top of the stack element is :",topelement)
#To remove the element from the stack
poppedelement = stack.pop()
print("Removed element from the stack:",poppedelement)
print(stack)
#To know the the stack is empty or not
s = not bool(stack)
print(s)
#To know the length of the stack
n = len(stack)
print(n)
# To know the the stack is empty or not
is_empty = len(stack) == 0
print(is_empty)



#To create a stack using deque
from collections import deque
stack = deque()
#To add elements to the stack
stack.append('Venkata Ramana')
stack.append('Rohini')
stack.append('Akhila')
stack.append('Kishor')
stack.append('Naya sri')
print("Family of Kalagarla's:",stack)
#To print peek element from the stack
topelement = stack[-1]
print("Top of the stack element is :",topelement)
#To remove the element from the stack
poppedelement = stack.pop()
print("Removed element from the stack:",poppedelement)
print(stack)



# Code using LIFOQueue
from queue import LifoQueue
stack = LifoQueue()
#to take the max size of the stack
stack = LifoQueue(maxsize=5)
#To add elements to the stack
stack.put('Venkata Ramana')
stack.put('Rohini')
stack.put('Akhila')
stack.put('Nandu')
stack.put('Naya sri')
print("Family of Kalagarla's:",list(stack.queue))
#To print peek element from the stack
topelement = stack.queue[-1]
print(topelement)
print(list(stack.queue))
#To remove the element from the stack
poppedelement = stack.get()
print(poppedelement)
print(list(stack.queue))
#To know the the stack size 
n = stack.qsize()
print(n)
# #To know the the stack is empty or not
a = stack.empty()
print(a)




# creating a dedicated Stack class provides better encapsulation and additional functionality:
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

mystack = Stack()
mystack.push('Chitti babu')
mystack.push('kantham')
mystack.push('Ajay')
mystack.push('Pushpa')
mystack.push('Surimma')
print("Family of Kolli's:",mystack.stack)
print("peek element",mystack.peek())
print("popped element:",mystack.pop())
print("length of the stack:",mystack.size())
print("Stack is empty or not:", mystack.isEmpty())
print("Stack after operations:", mystack.stack)



#Create a stack and perform stack operations using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top is None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.data
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
mystack = Stack()


