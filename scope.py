# #Local scope:-
# def hi():
#     name = "Akki"
#     print("Hello",name) # Hello Akki
# hi()

# #Global Scope
# x = 10
# def show():
#     x = 2
#     print(x)

# show()
# x = 5
# print(x)

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
