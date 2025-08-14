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
'''
#To create a stack
stack = []
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