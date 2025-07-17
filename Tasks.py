#Task 1 :- 16/07/2025
'''Convert to Uppercase'''
a = "Akhila"
print(a.upper()) # AKHILA
print(a.lower()) # akhila
a = "akhila"
print(a.capitalize()) # Akhila
a = " akhila kalagarla "
print(a.title()) # Akhila Kalagarla
print(a.count("a")) # 6
print(a.replace("kalagarla", "akki")) # akhila akki
print(a.startswith("akhi")) # True
print(a.endswith("garla")) # True
print(a.find("kalagarla")) # 8
print(a.strip()) # akhila kalagarla
a = "Akhila"
k = "-"
print(k.join(a)) # A-k-h-i-l-a
print(a.center(20,"*")) # *******Akhila*******
print(a.ljust(10,"-")) # Akhila----
print(a.rjust(15,"+")) # +++++++++Akhila

'''to check the string is in lower or not'''
n = "akhila"
a = n.lower()
if n == a:
    print("True")
else:                # True
    print("False")
'''To check the given string is palindrone or not'''
a = "madam"
if a == a[::-1]:
    print("palindrome")
else:                # palindrome
    print("not")
'''Remove first and last character'''
a = "Akhila"
print(a[1:-1:]) # khil
'''To reverse a string'''
a = "Akhila"
print(a[::-1]) # alihkA

# Hacker Ranker Question
n = int(input())
if n % 2 != 0:
    print("weird")
elif n % 2 == 0 and 2 <= n <=5:      
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <=20:
    print("Weird")
else:
    print("Not Weird")

#Task-2 on list slicing :- 17/07/2005
'''1Q'''
a = [0,1,2,3,4,5,6,7,8,9]
print(a[-7:-2:2]) # [3, 5, 7]
'''2Q'''
a = [1,2,3,4,5,6,7]
print(a[5:1:-1]) # [6, 5, 4, 3]
'''3Q.'''
a = ['a','b','c','d','e','f']
print(a[::2][1:]) # ['c','e']
'''4Q.'''
a = [1,2,3,4,5]
print(a[-400:3]) # [1, 2, 3]
'''5Q.'''
a = [1,2,3,4,5]
print(a[::-2]) # [5, 3, 1]
