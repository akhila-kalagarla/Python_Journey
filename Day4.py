# #DAY - 4 4/07/25
# #Range():
for i in range(5):
    print(i,end = ",") #0,1,2,3,4,
print()
#Ex:-
for i in range(1,10):
    print(i,end = " ") #1 2 3 4 5 6 7 8 9 
print()
#To print even numbers without % and if condition
for i in range(2,11,2):
    print(i, end = " ") #2 4 6 8 10
print()
#To print odd numbers without % and if condition
for i in range(1,10,2):
    if i == 9:
        print(i,".")
    else:
        print(i, end = " , ") #1 3 5 7 9
print()

#Loop control statements
for i in range(10):
    if i == 5:
        print(f"{i}.")
        break
    print(i,end = ",")

#Example on while loop
while True:
    a = input()
    if a == "exit":
        break
    print("you typed",a)

#Password code
a = input()
if a == "akhila@5":
    print("valid")
else:
    print("Invalid")

#Password using while
while True:
    a = input()
    if a == "akhila@5":
        print("Correct password")
        break
    print("Wrong password")

#Skip negative numbers
n = [4,-1,6,-2,0,9]
for i in n:
    if i < 0:
        print(f"Negative number :{i}")
        continue
    print(f"positive number :{i}")

#Stop printing characters on space
text = "Akhila good girl"
for char in text:
    if char == ' ':
        break
    print(char,end="")

#Skip vowels
text = "education"
vowels = "aeiou"
for char in text:
    if char in vowels:
        continue
    print(char)

#Break on first number > 20
n = [5,10,15,20,25,30]
for num in n:
    if num > 20:
        break
    print(num)

#Continue even numbers
for i in range(1, 21):
    if i%2 == 0:
        continue
    print(i, end = " ")

#Break in while loop
i = 1
while True:
    if i == 7:
        break
    print(i, end = " ") #1 2 3 4 5 6 
    i += 1

#Continue in while loop
i = 0
while i < 10:
    i += 1
    if i == 3 or i == 6:
        continue
    print(i, end = " ") #1 2 4 5 7 8 9 10 

#Break if total sum > 100
n = [10,20,30,40,15,5,7 ]
t = 0
for num in n:
    t += num #10+20=30
    if t > 100:
        break
    print("Sum:",t, end = ",") #Sum: 10,Sum: 30,Sum: 60,Sum: 100,

#Skip words starting with 'b'
string = ["bat","apple","banana","cat","dog"]
for word in string:
    if word.startswith('b'):
        continue
    print(word,end = " ") #apple cat dog 

#Nested loop with break
for i in range(1,4):
    for j in range(1,10):
        if i*j > 20:
            break
        print(f"{i}*{j}={i*j}")
    print()

#Find  first even and break
num = [1,3,5,7,8,9]
for nums in num:
    if nums%2 == 0:
        print("First even:",nums) #First even: 8
        break

#Continue on divisible by 4 or 6
for i in range(1,15):
    if i%4 == 0 or i%6 == 0:
        continue
    print(i, end = " ") #1 2 3 5 7 9 10 11 13 14 
print()

#Continue on divisible by 4 or 6
for i in range(1,15):
    if i%4 == 0 and i%6 == 0:
        continue
    print(i, end = " ") #1 2 3 4 5 6 7 8 9 10 11 13 14 
print()

#Skip every third character
text = "abcdefghijklmnopqrstuvwxyz"
for index, char in enumerate(text, 1):
    if index%3 == 0:
        continue
    print(char, end = " ") #a b d e g h j k m n p q s t v w y z 