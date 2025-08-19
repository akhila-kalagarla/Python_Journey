import Mymodule 
print(Mymodule.greet("Akhila"))  # Hello Akhila, welcome to kiet-world
print(Mymodule.add(5, 10))  # 15

from Mymodule import greet, add
print(greet("Hemanth sir"))  # Hello Hemanth sir, welcome to kiet-world
print(add(5, 10))  # 15

import calculator as c
print(c.add(5, 10))  # 15
print(c.subtract(10, 5))  # 5
print(c.multiply(5, 10))  # 50
print(c.divide(10, 2))  # 5.0
print(c.modulus(10, 3))  # 1
print(c.exponent(2, 3))  # 8

from calculator import add, subtract, multiply, divide, modulus, exponent
print(add(5, 10))  # 15 
print(subtract(10, 5))  # 5
print(multiply(5, 10))  # 50
print(divide(10, 2))  # 5.0
print(modulus(10, 3))  # 1
print(exponent(2, 3))  # 8  
