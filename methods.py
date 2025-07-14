#String 
'''A string is a squence of characters enclosed in single (''), double (""), or triple quotes (''' ''').
Strings are immutable, meaning their characters cannot be changed once created'''
str = '''hello'''
print(type(str))

#String operations
#Access:
s = "Hello world"
print(s[0]) # H
print(s[0:5]) # Hello
print(s+"!") # HEllo world!
print(s*2) # Hello worldHello world