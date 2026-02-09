def fun():
    print("Hii")
fun()

def evenodd(x):
    if x % 2 == 0:
        print(x, "is even number")
    else:
        print(x, "is odd number")
x = int(input("enter a number:"))
evenodd(x)

### 1.Default Arguments
def fun(x, y = 50):
    print("x:", x)
    print("y:", y)
fun(25)
### 2.Keyword Arguments
def fun(fname, lname):
    print("First Name:", fname)
    print("last Name:", lname)
fun(lname = "Kalagarla", fname = "Akhila")
### 3.Positional Arguments 
def fun(name, age):
    print("Name:", name)
    print("Age:", age)
fun("Akhila", 20)
### 4.Aribitary Arguments
def fun(*args):
    for arg in args:
        print(arg)
fun("Akhila", "Rohini", "Naya sri", "Kishor", "Venkata Ramana")
### 5.Aribitary Keyword Arguments
def fun(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)
fun(name="Akhila", age=20, city="Hyderabad")

### Function with functions 
def fun():
    a = "Hello"
    def fun1():
        print(a)
    fun1()
fun()

### Anonymous Functions
def fun(x): return x*x*x 
a = lambda x: x*x*x 
print(fun(3))
print(a(3))

### EXAMPLES 
def sq(x):
    return x*x 
print(sq(5))

def a(num):
    return num**2
print(a(4))

### Recursive Functions 
def fact(n):
    if n == 0:
        return 1 
    else:
        return n * fact(n-1)
a = int(input("Enter a number:"))
print(fact(a))