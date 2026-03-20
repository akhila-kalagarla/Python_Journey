x = 5
print(x)
y = x 
x = "Geeks"
print(x,y)
y = "computer"
print(x,y)

# Swapping of 2 variables
a = 5
b = 7
a, b = b, a
print(a, b) # Output: 7 5

# To count characters in a string
a = "Akhila"
c = 0 
for i in a:
    c += 1
print(c) # Output: 6 
#OR
print(len(a)) # Output: 6

import keyword
print("The list of keywords is : ")
print(keyword.kwlist)

for i in range(5):
    if i == 3:
        pass  
    else:
        print(i)

### Local Variable
def greet():
    msg = "Hello!"
    print("Inside function:", msg)

greet()
# print("Outside function:", msg)

### Global Variable 
msg = "HELLO All"
def greet():
    print("Inside Function :", msg)
greet()
print("Outside function :",msg)

### Use both local and global variables 
def greet():
    msg = "Hello all!"
    print("Local msg :", msg)
msg = "Hello all!"
greet()
print("Global Msg :", msg)

msg = "Hello all"
def greet():
    global msg 
    msg += "I am Akhila"
    print(msg)
    msg = "Good evening"
    # print(msg)
greet()
print(msg) 