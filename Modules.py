#Modules in python 
'''Modules are files containing Python code. They can define functions, classes, and variables that can be reused in other Python programs.
You can import a module using the import statement.'''
import math as m
print(m.sqrt(16))  # 4.0
print(m.pi)         # 3.141592653589793
print(m.factorial(5))  # 120
from math import floor, ceil
print(ceil(3.7))  # 4
print(floor(3.7))  # 3