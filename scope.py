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
