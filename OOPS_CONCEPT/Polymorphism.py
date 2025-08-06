'''Polymorphism - 
 Poly :- Many, 
 morphism :- Ways
 In polymorphism we have 4 types - 1) Compile time Polymorphism(Method overloading) - It execute the code in compilation time
                                   2) Run time Polymorphism(Method overriding) 
                                   3) Operator overloading
                                   4) Duck typing '''
# DUCK TYPING EXAMPLE
class Animal:
    def sound(self):
        print("Animal makes sound")
class dog:
    def sound(self):
        print("Bark")
class cat:
    def sound(self):
        print("Meow")
def get_sound(Animal):
    Animal.sound()
get_sound(dog()) # Bark
get_sound(cat()) # Meow

# METHOD OVERLOADING 
class grandparent:
    def add(self,a = 1,b = 0,c = 0):
        return a+b+c
s = grandparent()
print(s.add())
print(s.add(5))
print(s.add(4,10))
print(s.add(3,2,9))
