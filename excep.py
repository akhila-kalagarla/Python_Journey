# Exception handling
'''Handling the errors without getting any errors in output, 
   and some examples on this concept'''

'''1.example on zerodivision error'''
a = int(input())
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("zero")
'''2.To check your age is valid or not using try,except block'''
age = int(input("Enter your age:")) # 61
try:
    if age < 18:
        raise ValueError
    else:
        print("The age",age, "is valid") # The age 61 is valid
except:
    print("The age",age, "is not valid")
'''3.Example on try, except, finally'''
try:
    fileptr = open('file.txt',"r")
    try:
        fileptr.write("Hi i am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")
'''4.'''
class errorincode(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
try:
    raise errorincode(2000)
except errorincode as ae:
    print("Received error:",ae.data)