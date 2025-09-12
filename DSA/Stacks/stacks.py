class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!")
        else:
            res=self.stack.pop()
            return res
    def peek(self):
        if self.isEmpty():
            print("stack is Empty!")
        else:
            return self.stack[-1]
        
st=Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.stack)
print(st.pop())
print(st.stack)


# ### Another Example
# class Gatestudents:
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)

#     def pop(self):
#         if len(self.stack) == 0:
#             return "Stack is empty"
#         return self.stack.pop()

#     def peek(self):
#         if len(self.stack) == 0:
#             return "Stack is empty"
#         return self.stack[-1]

#     def isEmpty(self):
#         return len(self.stack) == 0

#     def size(self):
#         return len(self.stack)


# mystack = Gatestudents()
# mystack.push('Venakataramana')
# mystack.push('Rohini')
# mystack.push('Akhila')
# mystack.push('Nandu')
# mystack.push('Naya Sri')

# print("Popped:", mystack.pop())
# print("Peek:", mystack.peek())
# print("Is Empty?", mystack.isEmpty())
# print("Size:", mystack.size())
# print("Students in the gate:", mystack.stack)
