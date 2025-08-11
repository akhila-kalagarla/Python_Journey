'''OVERRIDING - sub class rewrites the parent class code'''
#Inheritance
'''Definition: Inheritance is a fundamental concept in object-oriented programming that allows one class (the child or subclass) to inherit
attributes and methods from another class (the parent or superclass).
This promotes code reuse and establishes a hierarchical relationship between classes, enabling the creation of more specialized classes based on existing ones.
Inheritance allows subclasses to extend or modify the behavior of their parent classes, enabling polymorphism and dynamic method resolution.
It is a key feature of OOP that supports the creation of complex systems by building on existing code, reducing redundancy, and enhancing maintainability.
Inheritance is classified into 5 types:
   - 1)Single
   - 2)Multilevel
   - 3)Multiple
   - 4)Hierarchial
   - 5)Hybrid'''
#Example on Single Inheritance
class parent:
    def greet(self):
        print("Hello from parent")
class child(parent):
    def greek(self):
        print("Hello from child")
obj = child()
obj.greet() # Hello from parent
obj.greek() # Hello from child

#Example on Multilevel Inheritance
class grandparent:
    def greet(self):
        print("Hi from grandparent")
class parent(grandparent):
    def greek(self):
        print("Hi from parent")
class child(parent):
    def greeks(self):
        print("Hi from child")
obj = child()
obj.greeks() # Hi from child
obj.greek() # Hi from parent
obj.greet() # Hi from grandparent

#Multi level Inheritance without inheriting it's parent class
class grandparent:
    def greet(self):
        print("Hi from grandparent")
class parent:
    def greek(self):
        print("Hi from parent")
class child:
    def greeks(self):
        print("Hi from child")
obj = child()
obj.greeks() # Hi from child

#Example on Multiple Inheritance
class grandparent:
    def greet(self):
        print("Hi from grandparent")
class parent:
    def greek(self):
        print("Hi from parent")
class child(grandparent, parent):
    pass
obj = child()
obj.greek() # Hi from parent
'''Or'''
class grandparent:
    def greeks(self):
        print("Hi from grandparent")
class parent:
    def greek(self):
        print("Hi from parent")
class child(grandparent, parent):
    def greet(self):
        print("Hii from child")
obj = child()
obj.greet() # Hii from child
obj.greek() # Hi from parent
obj.greeks() # Hi from grandparent

#Example on Hierarchial inheritance - Using parent class we write multiple sub classes
class parent:
    def greet(self):
        print("Hello from parent")
class child(parent):
    def feature1(self):
        print("feature1 from child1")
class child2(parent):
    def feature2(self):
        print("feature2 from child2")
obj1 = child()
obj2 = child2()
obj1.greet() # Hello from parent
obj1.feature1() # feature1 from child1
obj2.greet() # Hello from parent
obj2.feature2() # feature2 from child2

# Using super keyword to print the output from the parent class and sub class
class humans:
    def greet(self):
        print("Hi from humans")
class car(humans):
    def greet(self):
        super().greet()
        print("i am in house")
obj = car()
obj.greet()

'''Example on Inheritance'''
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

