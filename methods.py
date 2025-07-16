#String 
'''A string is a squence of characters enclosed in single (''), double (""), or triple quotes (''' ''').
Strings are immutable, meaning their characters cannot be changed once created'''
str = '''hello'''
print(type(str))

#String operations
#Access:
s = "Hello world"
print(s[0]) # H
'''Slicing'''
print(s[0:5]) # Hello
'''Concatination'''
print(s+"!") # Hello world!
'''Repetation'''
print(s*2) # Hello worldHello world

#String methods
'''Upper()'''
s = "hello"
print(s.upper()) # HELLO
'''lower()'''
s = "HELLO"
print(s.lower()) # hello
'''Replace()'''
s = "Hello"
print(s.replace('o','l')) # Helll
'''strip()'''
s = " Hello motto "
print(s.lstrip())
print(s.rstrip())
print(s.strip())
'''split(',')'''
a = 'a,b,c'
print(*a.split(',')) # ['a', 'b', 'c']
'''find()'''
a = "Akhila"
print(a.find('l')) # 4
'''isalpha()'''
a = "abc"
print(a.isalpha()) # True
'''Capitalize()'''
a = "akhila"
print(a.capitalize()) # Akhila
'''Title()'''
a = "akhila kalagarla"
print(a.title()) # Akhila Kalagarla
'''Swapcase()'''
a = "AkHILa"
print(a.swapcase()) # aKhilA
'''Remove()'''
a = "Akhila kalagarla"
print(a.removesuffix("kalagarla"))  # Akhila

a = "AkhilaKalagarla"
b = a.removeprefix("Akhila") # Kalagarla
print(b)

'''isnumeric'''
a = "1234"
print(a.isnumeric()) # True
a = "akki41"
print(a.isalnum())
a = "120"
print(a.isdigit())
a = "8421"
print(a.isdecimal())
a = "AKHILA"
print(a.isupper())
a = "akhila"
print(a.islower())
a = "Akhila Kalagarla"
print(a.istitle())

#Date : 16/07/2025, day - 10
'''Slicing'''
'''
Syntax:- string[start:end:step]
start --> index to begin slice
end --> index to end slice
step --> optional; step/jump size
'''

#Ex:-
s = "kiet students"
print(s[0:6]) # kiet s
print(s[1::]) # iet students
print(s[:5:]) # kiet
print(s[::2]) # ke tdns
print(s[0:9:3]) # ktt
'''Reverse slicing'''
s = "Kiet students"
print(s[-1::]) # s
print(s[::-1]) # stneduts teiK
print(s[:-3:]) # Kiet stude
print(s[-1:-5:-1]) # stne
s = "kietwcollegestudents"
print(s[:-10:]) # kietwcolle