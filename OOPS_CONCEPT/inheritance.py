'''OVERRIDING - sub class rewrites the parent class code'''
#Inheritance
'''-One class inherits properties/methods of another
   Inheritance is classified into 2 types
   - 1)Single
   - 2)Multilevel
   - 3)Multiple
   - 4)Hierarchial
   - 5)Hybrid'''
#Example on Single inheritance
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

#Example on Hierarchial inheritance

#Example on Hybrid inheritance

'''Example for inheritance concept'''
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