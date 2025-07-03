###Numeric data types
a = 10
print(a) #10
a = 10
print(type(a)) #<class 'int'>
a = 10.5
print(a) #10.5
print(type(a)) #<class 'float'>
a = 5+3j
print(a) #(5+3j)
print(type(a)) #<class 'complex'>

###Text data type
name = 'Akhila' 
quote = "old is gold"
multi = '''This is a multi line string'''
print(name) #Akhila
print(quote) #old is gold
print(multi) #This is a multi line string
print(type(name)) #<class 'str'>
print(type(quote)) #<class 'str'>
print(type(multi)) #<class 'str'>

###Set data types - Unorderd,{},Unique
set = {1,2,5,2,4}
print(set) #{1, 2, 4, 5}

###Boolean data type
a = 2
print(bool(a)) #True
a = []
print(bool(a)) #False

###Sequence data types
#LIST - [],Mutable,Ordered
list = [10,20,"kiet",30]
print(list) #[10, 20, 'kiet', 30]
print(list[0]) #10
list[0] = 80
print(list) #[80, 20, 'kiet', 30]
#TUPLES - (),Ordered, Immutable
tup = (10,20,"kiet",50)
print(tup) #(10, 20, 'kiet', 50)

###Mapping data type
#Dictionary - {}, keys:values, keys-immutable, values-mutable
dict = {"name":"Akhila","age":42}
print(dict) #{'name': 'Akhila', 'age': 42}
print(dict.values()) #dict_values(['Akhila', 42])
print(dict.keys()) #dict_keys(['name', 'age'])
print(dict.items()) #dict_items([('name', 'Akhila'), ('age', 42)])

###Inputs and Outputs
#####Inputs
#To take int as input
a = int(input("Enter a number:")) #Enter a number:6
b = int(input("Enter a number:")) #Enter a number:7
print(a) #6
print(b) #7
print(a+b) #13
#To take string as input
name = input("Enter your name: ") #Enter your name: Akhila
print("Hi", name) #Hi Akhila
#To take multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split() #6 9
print(x) #6
print(y) #9
print(x, y) #7 8

#####Outputs
#Simple output
print("Hello, World!")
print("Welcome","to","python","language", sep = "-")
print("Loading", end = "...")

#Comments
#####Single line comment
#starts with # symbol
print("hi")#This msg not print #hi
#####Multi line comment
'''This is multi line  comment python ignores this multi line comments'''

#DAY - 2/07/2025
###Conditional statements
#if()
x = 10
if x>5:
    print(x,"is greater than 5") #10 is greater than 5
#Examples:-
x = int(input()) #4
if x > 0:
    print(x,"is positive number") #4 is positive number

x = int(input()) #-4
if x < 0:
    print(x,"is negative number") #-8 is negative number

x = 15
if x % 3 == 0 and x % 5 == 0:
    print(x,"is divisible by both 3 and 5") #15 is divisible by both 3 and 5

x = 16
if x % 2 == 0 and x % 8 == 0:
    print(x,"is divisible by both 2 and 8") #16 is divisible by both 2 and 8

#if...else
#Examples
x = 3
if x>5:
    print(x,"is greater than 5")
else:
    print(x,"is smaller than 5") #3 is smaller than 5

#Even or odd
x = int(input())
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Positive or Negative
x = int(input())
if x > 0:
    print("postive")
else:
    print()

#to check a person is eligible or not to vote
x = int(input()) #54
if x >= 18:
    print("eligible") #eligible
else:
    print("not eligible")

#To print the largest number among two numbers
a = int(input()) #24
b = int(input()) #32
if a > b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a) #32 is greater than 24

#Password checking
x = input()
b = "Akhila@12345"
if x == b:
    print("Valid")
else:
    print("Invalid")

#To check in string there is vowel or not
x = input()
y = x.lower()
a = "aeiou"
if y in a:
    print("Vowels")
else:
     print("Consonant")

#Leap year
x = int(input())
if (x % 4 == 0 and x %100 != 0) or (x % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

#Fail or Pass
x = int(input())
y = 35
if x > y:
    print("Pass")
else:
    print("Fail")

#elif 
a = 5
b = 2
c = 1
if a > b and a > c:
    print(a,"is bigger number")
elif b > a and b > c:
    print(b,"is bigger number")
else:
    print(c,"is bigger number")

#Grading system
a = int(input())
if a > 90:
    print("A Grade")
elif a > 75:
    print("B Grade")
elif a > 50:
    print("C Grade")
elif a > 40:
    print("D Grade")
elif a >= 35:
    print("E Grade")
else:
    print("Fail")

#To check whether the person is child, adult, citizen or teenage
a = int(input())
if a > 0 and a <= 12:
    print("Child")
elif a >= 13 and a <= 19:
    print("Teenage")
elif a > 19 and a <= 35:
    print("Adult")
else:
    print("Citizen")

#Small application on python for beginners
num1 = int(input("Enter a price"))
if num1 >= 500:
    print("50% discount will applicable for on your purchase")
elif num1 >= 300:
    print("35% discount will be applicable on your purchase")
elif num1 >= 200:
    print("20% discount will be applicable for on your purchase")
elif num1 >= 100:
    print("10% discount will be applicable on your purchase")
else:
    print("0% discount")

#DAY - 3 3/07/2025
#Looping statements(Iteration)
#example using break
for i in range(5): #0 1 2 
    if i == 3:
        break
    print(i)
#or
for i in range(5): #0 1 2 3
    print(i, end = " ")
    if i == 3:
        break

#Example using continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# for loop using list
list = [10,20,30,40,50]
for i in list:
    print(i)
list = ["akki","kishu","naya","bharath"]
for i in list:
    print(i)

#Even number code
l = [10,20,30,40]
for i in l:
    if i % 2 == 0:
        print(i)
#Odd number code
l = [10,20,30,40]
for i in l:
    if i % 2 != 0:
        print(i)

#To print even numbers without % and if condition
for i in range(1,10,1):
    print(i, end = " ")
##To print odd numbers without % and if condition
for i in range(1,10,2):
    print(i, end = " ")

#To print the number is negative or postive
z = int(input())
n = int(input())
for i in range(z, n+1):
    if i >= 0:
        print(i,"positive")
    else: 
        print(i,"Negative")

#To print a table
n = int(input())
for i in range(1,11):
    print(n, "*", i, "=", n*i)
# Or
for i in range(1,11):
    for j in range(1,11):
        print(j, "*", i, "=", i * j, end = "\t")
    print()

num = int(input())
nums = abs(num)
c = 0
for i in str(nums):
    c += int(i)
print(f"Sum is :{c}")

#While Loop
c = 0
while c < 5:
    if c == 3:
        c += 1
        continue
    print(c)
    c += 1

c = 6
while c > 0:
    print(c)
    c -= 1


    
