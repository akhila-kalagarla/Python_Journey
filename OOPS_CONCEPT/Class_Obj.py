#A class and object  in OOPs
'''Class : A blueprint for objects
   object : An instancenof the class
Class is a collection of attributes and methods that define the properties and behaviors of an object.
   Attributes are variables that hold data, and methods are functions that define the behavior of the object.
Objects are instances of a class that can access the attributes and methods defined in the class.
   Objects are created from classes, and they can have their own unique data while sharing the same structure and behavior defined by the class.
Classes encapsulate data and functionality, allowing for better organization and modularity in code.
   Objects can interact with each other and with the outside world through their methods, allowing for complex behaviors and interactions.
A class can have multiple objects, and each object can have its own state (data) while sharing the same structure (methods).
    Classes can also inherit from other classes, allowing for code reuse and the creation of more specialized classes.'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"hello my name is {self.name} and i am {self.age} years old")
p1 = person("Akhila",20)
p2 = person("Pushpa",21)
print(p1.name) # Akhila
print(p2.name) # Pushpa
p1.greet() # hello my name is Akhila and i am 20 years old
p2.greet() # hello my name is Pushpa and i am 21 years old

#Polymorphism
'''Same method name, different behavior based on object'''
class Cat:
    def sound(self):
        print("Cat meows")
class Cow:
    def sound(self):
        print("cow moos")
def sounds(animal):
    animal.sound()
sounds(Cat())
sounds(Cow())

# Abstraction
'''Hiding complex logic, showing only important information'''
from abc import ABC, abstractmethod
class vehical(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(vehical):
    def start(self):
        print("Bike started")
b = Bike()
b.start() # Bike started

'''Real time example to understand the oops concept'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Buddy says Woof!
cat.speak()  # Whiskers says Meow!

''' Simple example'''
print()
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)

# Creating objects
student1 = Student("Akhila", 101)
student2 = Student("Nandu", 102)

# Calling method
student1.display_info()
print("------------------")  # Just to add a blank line
student2.display_info()

'''Simple examples for creating classes and objects in OOPs'''
class car:
    speed = "100kmph"
    colour = "White"
car1 = car()
print(car1.colour) # White
print(car.colour) # White
'''2.'''
class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
car1 = car("Volvo","Black")
car2 = car("Royal","Grey")
print(car1.colour) 
print(car2.name) 
'''3.'''
class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def cardetails(self,weight,speed):
        print(f"{weight}kg,{speed}km/h")
car1 = car("bmw","white")
# print(car1.colour)
car1.cardetails(250,"100kmph") # 250kg,100kmphkm/h
'''4.'''
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def studetails(self,nickname,rollno):
        print(f"I am {nickname} and my roll no is {rollno}")
p1 = student("Akhila",20)
print(p1.name) # Akhila
print(p1.age) # 20
p1.studetails("Akki","22JN1A4506") # I am Akki and my roll no is 22JN1A4506
'''5.'''
class car:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def vehical(self):
        print("The car spped and colour:",self.name,",",self.colour)
car1 = car("BMW","white")
car2 = car("AUDI","Blue")
print(car1.name) 
print(car2.name) 
car1.vehical() 
car2.vehical() 
'''Class method'''
class student:
    number = 5
    @classmethod # To define the class is only class we use classmethod
    def update(cls, count):
        cls.number = count
student.update(6)
print(student.number) # 6
'''static method'''
class student:
    @staticmethod # To define the class is static we use staticmethod
    def hello():
        print("I am Akhila")
student.hello() # I am Akhila