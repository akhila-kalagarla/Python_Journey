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

