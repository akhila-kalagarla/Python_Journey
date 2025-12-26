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

# To check whether a number is even or odd
num = int(input("Enter a number:"))
print("even" if num%2==0 else "odd")

# To give suggestions based on weather using match case
weather = input("Enter the weather(sunny/rainy/cold/hot/cloudy):").lower()
match weather:
    case "sunny":
        print("Good for travelling")
    case "rainy":
        print("Not good for planning a trip")
    case "cold":
        print("Carry warm clothes")
    case "hot":
        print("Stay hydrated")
    case "cloudy":
        print("Might rain today") 
    case _:
        print("Invalid weather type")

# write a loop to jump in powers of 2 from 1 to 10 using function and while loop()
def powers_of_two():
    i = 1
    while i <= 10:
        print(i)
        i *= 2
powers_of_two()

# Input: x = 10
# Output: 1 4 9
# Explanation:From 1 to 10, numbers in powers of 2 are, 12, 22, 32 as 1, 4 and 9.
def num(x):
    i = 1
    while i*i <= x:
        print(i*i, end=" ")
        i += 1 
    return ""
x = int(input())
print(num(x))

# You are given a number n, take input of n and print its multiplication table in a single line using for loop till n * 10. 
# Examples:
# Input: n = 5
# Output: 5 10 15 20 25 30 35 40 45 50
n = int(input())
for i in range(1, 11):
    print(n*i, end = " ")

# You are given a string s, you need to print its characters at even indices(index starts at 0).
# Examples:
# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea
def a(S):
    for i in range(0, len(S), 2):
        print(S[i], end = "")
S = input()
print(a(S))

# Input: x = 3
# Output: 3 2 1 0
# Explanation:
# Numbers in decreasing order from 3
# are 3, 2, 1, 0.
def a(x):
    i = x 
    while (x >= 0):
        print(x, end = " ")
        x -= 1
    return "" 
x = int(input())
print(a(x))

# Given an integer n, write a program to print the square of size n using "*" character. 
# Examples :
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *
# Explanation: It's a square! Each side contains n = 4 .
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# factorial of a number
class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
obj = Solution()
n = int(input())
print(obj.factorial(n))
