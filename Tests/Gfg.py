#To remove special symbols from the given text
def process(text):
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    text = text.strip()
    return text
result = input("Enter a text:")   #Enter a text:###Hello i am Akhila from @Kiet-W with the roll no: 22JN1A4506,!
print(process(result)) #Output: Hello i am Akhila from KietW with the roll no 22JN1A4506

#To print a,c values
def num(a,b,c):
    print(a)
    #print(b)
    print(c)
    return [a,c]
a = int(input())
b = int(input())
c = int(input())
print(num(a,b,c)) #[a,c] values will be printed 

#Swapping of 2 variables
x = 5
y = 6
temp = x
x = y
y = temp
print(x)
print(y)
  #Or
x, y = y, x
print(x)
print(y)
  #Or
x = x + y
y = x - y
x = x - y
print(x)
print(y)

# #Expressions on the right-hand side are evaluated before assignment:
x = 100
y = "Akhila"

x, y = x - 1, y + "6"
print(x)
print(y)

# To check Truthy values
x = 7
if x:
  print(x,"is a number")

x = 0
if x:
   print(x,"is a number")

# Print the min or max numbers using ternary operator 
a, b = 10, 20 
min = a if a<b else b 
print(min) 
max = a if a>b else b 
print(max)

# Walrus operator example in python 3.8
num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())
print(num)
#
a = [{"id":1, "name":"Akhila", "age":20},
     {"id":2, "name":"Nandu", "age":19},
     {"id":3, "name":"Naya", "age":10}]
for i in a:
    if name:= i.get("name"):
        print(name)
print("Without walrus operator:")
for i in a:
    name = i.get("name")
    if name:
        print(name)
###
food = []
while True:
    f = input("Enter your fav food")
    if f == "Stop":
        break 
    food.append(f)
print(food)
# Using Walrus operator 
food = []
while (f := input("enter your fav food (or type stop to end):")) != "stop":
    food.append(f)
print(food)

# Ternary conditional statement 
age = 18
c = "adult" if age >= 18 else "minor"
print(c)

# To check if the user has sufficient balance to buy a product 
balance = float(input("ENTER YOUR BALANCE:"))
price = float(input("ENTER THE PRICE OF THE PRODUCT:"))
if balance >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")

# Write a program to login to a website using username and password 
username = input("Enter your username:")
password = input("Enter your password:")
if username == "admin" and password == "12334567":
    print("Login successfull")
else:
    print("Check your credentials")
###
username = input("enter username:")
password = input("enter password:")
if username == "admin":
    if password == "122334455":
       print("login successful")
    else:
        print("Incorrect password")
print("username not found")

###To chech wether the student is passes with scholarship or not 
marks = int(input("Enter your marks:"))
if marks >=40:
    if marks >= 80:
        print("You have passed with scholarship")
    else:
        print("You have passed without scholarship")
else: 
    print("You have failed")