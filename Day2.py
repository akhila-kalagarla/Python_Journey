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

