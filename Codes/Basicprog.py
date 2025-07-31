# 1.Write a Python program to check whether a number is even or odd.
number = int(input("Enter a number:"))
if (number%2 == 0):
    print("Even")
else:
    print("Odd")

# 2.Write a program to find the largest of three numbers.
num1 = int(input("Enter a first number:"))
num2 = int(input("Enter a second number:"))
num3 = int(input("Enter a third number:"))
if(num1 > num2 and num1 > num3):
    print(num1,"is largest number")
elif(num2 > num1 and num2 > num3):
    print(num2,"is largest number")
else:
    print(num3,"is largest number")

# 3.Write a Python function that returns the factorial of a number.
def fact(nums):
    if nums == 0 or nums == 1:
        return 1
    else:
        return nums*fact(nums-1)
nums = int(input("Enter a number:"))
print("Factorial of", nums,"is", fact(nums))

# 4.Write a program to print all numbers from 1 to 100 that are divisible by 5.
for i in range(0, 101):
    if (i%5 == 0):
        print(i, end=" ")

# 5.Write a program that reverses a string entered by the user.
a = input("Enter a string:")
x = a[::-1]
print(x)

# 6.Write a program to check if a number is positive, negative, or zero.
num = int(input("Enter a number:"))
if (num > 0):
    print("positive")
elif (num < 0):
    print("negative")
else:
    print("Zero")

# 7.Write a Python program that accepts a user's age and tells if they are eligible to vote (18+).
age = int(input("Enter your age:"))
if (age > 18):
    print("You are eligible to vote")
else:
    print("Not eligible")

# 8.Take two numbers as input and print the maximum.
n = int(input("Enter a one number:"))
n1 = int(input("Enter a second number:"))
print(max(n, n1))

# 9.Write a program to check whether a character is a vowel or consonant.
charac = input("Enter a character:")
a = ["a","e","i","o","u"]
if charac in a:
    print("Vowel")
else:
    print("Consonant")

# 10.Write a program to determine whether a given year is a leap year.
year = int(input("Enter a year:"))
if (year%4 == 0):
    print("Leap year")
else:
    print("Not leap year")

# 11.Write a program to generate Fibonacci series up to n terms.
n = int(input("Enter a number:"))
a, b = 0, 1
for i in range(0, n+1):
    print(a, end = " ")
    a, b = b, a + b

# 12.Write a program to check whether a number is an Armstrong number.
num = int(input("Enter a number: "))
original_num = num
num_digits = len(str(num))
sum_of_powers = 0

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num = num // 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

# 13.Write a program to check whether a number is prime.
number = int(input("Enter a number:"))
for i in range(0, number+1):
    if(number%i == 0):
        print("Not prime")
    else:
        print("Prime")

# 14.Write a Python function to check whether a string is a palindrome.
a = "madam"
if (a == a[::-1]):
    print("Palindrome")
else:
    print("Not palindrome")

# 15. Write a python function to sort a list without using sort() 
def ascend(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list = [12, 4, 56, 1, 99, 23]
sorted_list = ascend(my_list)
print("Sorted list in ascending order:", sorted_list)

                         #OR

numbers = [6, 3, 8, 1, 4]
sorted_list = []
while numbers:
    smallest = min(numbers)    
    sorted_list.append(smallest)  
    numbers.remove(smallest)      
print("Sorted list:", sorted_list)

# 16.Write a python program to print the sum of numbers which are divisible by 3 or 5
N = int(input())
count = 0
for i in range(1, N):
    if i%3 == 0 or i%5 == 0:
        count += i
print(count)

# 17.Write a function that takes a string and returns the string with:All vowels removed Reversed string
def vowels(s):
    v = "aeiouAEIOU"
    n = ''.join([char for char in s if char not in v])
    return n[::-1]
s = "hello word"
print(vowels(s))

# 18.Given a tuple of numbers, write a function that returns a new tuple containing only even numbers.
def even(tup):
    return tuple(num for num in tup if num%2 == 0)
print(even((1,2,3,4,5,6)))

# 19.Write a Python program that: Takes two sets of integers as input Returns a set that contains elements present in the first set but not in the second
A = {1,2,3,4}
B = {3,4,5}

C = A - B
print(C)

# 20.Write a function that takes a dictionary of students and their marks and returns the name(s) of the student(s) with the highest marks.
def top(marks):
    scores = max(marks.values())
    return [name for name, score in marks.items() if score == scores]
students = {"Anil":88, "Sunil":92, "Priya":85, "Rekha":92}
print(top(students))

# To print sum of elements in a list
a = [3,5,2,8]
print(sum(a)) # 18
#OR
sum = 0
for i in a:
    sum += i
print(sum) # 18
#OR
n = int(input())
s = 0
a = list(map(int, input().split()))
for i in range(n):
    s += a[i]
print(s)

#Convert list to a tuple
a = ['apple','banana','mango']
print(tuple(a)) # ('apple', 'banana', 'mango')

# To print min and max
a = (1,2,3,4,5)
print(*a[:1:])
print(*a[-1::])
#OR
a = tuple(map(int, input().split()))
b = sorted(a)
print(*b[:1:])
print(*b[-1::])

# To print the count that a particular elements are repeated
a = (1,2,3,2,4,5,6,2)
print(a.count(2))

a = tuple(map(int, input().split()))
n = []
c = 1
for i in a:
    if i not in n:
        n.append(i)
    else:
        c += 1
print(*n)
print(c)