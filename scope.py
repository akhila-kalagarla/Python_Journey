#Local scope:-
def hi():
    name = "Akki"
    print("Hello",name) # Hello Akki
hi()

#Global Scope
x = 10
def show():
    x = 2
    print(x)

show()
x = 5
print(x)

#Enclosed scope(Non Local)
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Inner",x)
    inner()
    print("Outer",x)
outer()  

#Built - in scope
x = [1,2,3,4,5,6,7,8,9,]
print(len(x)) # 5
print(sum(x)) # 15
print(max(x)) # 5
print(min(x)) # 1

# *args
def greet(*args):
    for name in args:
        print("hello",name)
greet("Akki","Bharath","Nandu","Nayu")

def akki(*i):
    for num in i:
        if num % 2 == 0:
            print(num)
akki(1,2,3,4,5,6,7,8)

def show(*args):
    for items in args:
        print(items)

show(1,2,3)

# **kwargs
def students(**kwargs):
    print(kwargs)
students(name = "Akki", age = 19) # {'name': 'Akki', 'age': 19}

