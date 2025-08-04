'''OVERRIDING - sub class rewrites the parent class code'''
#Inheritance
'''-One class inherits properties/methods of another
   Inheritance is classified into 3types
   - 1)Single
   - 2)Multi
   - 3)Multilevel'''
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