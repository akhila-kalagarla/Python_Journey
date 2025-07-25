#A class and pbject  in oops
'''Class : A blueprint for objects
   object : An instanceof the class'''
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


# Encapsulation
'''Hiding internal data by making variables private'''
class student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    def details(self):
        return f"{self.__name} got {self.__marks} marks"
s1 = student("Akhila",95)
s2 = student("Nandu",98)
print(s1.details())
# print(s1.name)

#Inheritance
'''One class inherits properties/methods of another'''
class Animal:
    def speak(self):
        print("Animal sounds")
class dog(Animal):
    def speak(self):
        print("Dog barks")
class cat(Animal):
    def speak(self):
        print("cat Meow")
d = cat()
a = dog()
a.speak()
d.speak()

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