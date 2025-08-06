# '''Polymorphism - 
#  Poly :- Many, 
#  morphism :- Ways
#  In polymorphism we have 4 types - 1) Compile time Polymorphism(Method overloading) - It execute the code in compilation time
#                                    2) Run time Polymorphism(Method overriding) 
#                                    3) Operator overloading
#                                    4) Duck typing '''
# # DUCK TYPING EXAMPLE
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class dog:
#     def sound(self):
#         print("Bark")
# class cat:
#     def sound(self):
#         print("Meow")
# def get_sound(Animal):
#     Animal.sound()
# get_sound(dog()) # Bark
# get_sound(cat()) # Meow

# # METHOD OVERLOADING EXAMPLE
# class grandparent:
#     def add(self,a,b = 0,c = 0):
#         return a + b + c
# s = grandparent()
# print(s.add(5))
# print(s.add(4,10))
# print(s.add(6,2,9))

# #METHOD OVERRIDING 
# class parent:
#     def greek(self):
#         print("Hello from parent")
# class child:
#     def greek(self):
#         print("Hello from child")
# obj = child()
# obj.greek() # Hello from child

# Operator Overloading example
class stu:
    def __init__(self, marks):
        self.marks = marks 
    def __add__(self,others):
        return stu(self.marks + others.marks)
    def __str__(self):
        return str(self.marks)
s1 = stu(20)
s2 = stu(25)
s3 = stu(30)
s4 = stu(40)
s5 = stu(50)
s6 = stu(50)
print(s1 + s2 + s3 + s4 + s5 + s6) # 215
'''=====>'''
class stu:
    def __init__(self, marks):
        self.marks = marks 
    def __add__(self,others):
        return (self.marks + others.marks)
s1 = stu(20)
s2 = stu(25)

print(s1 + s2) # 45
