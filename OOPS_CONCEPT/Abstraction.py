'''#ABSTRACTION - Displaying only essential features and hiding unnecessary details
Definition: Abstraction is a fundamental concept in object-oriented programming that focuses on exposing only the necessary parts of an object while hiding the complex implementation details. 
This allows users to interact with objects at a higher level without needing to understand the underlying complexities.'''
#Difference between Abstraction and Encapsulation:
'''Abstraction is about hiding the complexity by providing a simplified interface, 
while encapsulation is about bundling the data and methods that operate on that data within a single unit (class).'''
#Diference ways to achieve abstraction in Python:
'''Abstraction can be achieved in Python through abstract classes and interfaces,
which allow you to define methods that must be implemented by subclasses, ensuring that the essential features are exposed while the implementation details remain hidden.
Abstract classes can be created using the `abc` module, which provides a way to define abstract base classes with abstract methods that must be implemented by any concrete subclass.
This allows for a clear separation of interface and implementation, promoting cleaner and more maintainable code.'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle Area:", circle.area())  # Circle Area: 78.5
print("Rectangle Area:", rectangle.area())  # Rectangle Area: 24
'''===>>>'''