'''#ABSTRACTION - Displaying only essential features and hiding unnecessary details
Definition: Abstraction is a fundamental concept in object-oriented programming that focuses on exposing only the necessary parts of an object while hiding the complex implementation details. 
This allows users to interact with objects at a higher level without needing to understand the underlying complexities.'''
#Difference between Abstraction and Encapsulation:
'''Abstraction is about hiding the complexity by providing a simplified interface, 
while encapsulation is about bundling the data and methods that operate on that data within a single unit (class).
Encapsulation restricts direct access to some of an object's components, which is a way to achieve abstraction.
    @abstractmethod is a decorator used to define abstract methods in an abstract class, which must be implemented by any concrete subclass.
and ensures that the method is declared but does not provide an implementation, forcing subclasses to provide their own implementation'''
#Diference ways to achieve abstraction in Python:
'''Abstraction can be achieved in Python through abstract classes and interfaces,
which allow you to define methods that must be implemented by subclasses, ensuring that the essential features are exposed while the implementation details remain hidden.
Abstract classes can be created using the `abc` module, which provides a way to define abstract base classes with abstract methods that must be implemented by any concrete subclass.
This allows for a clear separation of interface and implementation, promoting cleaner and more maintainable code.
'''
# Example of Abstraction using Abstract Base Class (ABC) in Python:
# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass 
#     @abstractmethod
#     def stop(self):
#         pass
#     @abstractmethod
#     def speed(self):
#         pass
#     @abstractmethod
#     def cost(self):
#         pass
# class car(vehicle):
#     def start(self):
#         print("Car started")
#     def stop(self):
#         print("Car stopped")
#     def speed(self):
#         print("Car speed is 100km/h")
#     def cost(self):
#         print("Car cost is 1,00,000")
# class bike(vehicle):
#     def start(self):
#         print("Bike started")
#     def stop(self):
#         print("Bike stopped")
#     def speed(self):
#         print("Bike speed is 60km/h")
#     def cost(self):
#         print("Bike cost is 95,000")
# c = car()
# b = bike()              
# c.start() # Car started
# c.stop() # Car stopped
# b.speed() # Bike speed is 60km/h
# b.cost() # Bike cost is 95,000

# Example of Abstraction Method 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
A = [Cat(),Dog()]
for i in A:
    print(i.sound())


