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