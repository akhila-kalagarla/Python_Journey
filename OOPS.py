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

