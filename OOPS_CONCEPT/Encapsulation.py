'''Encapsulation - Hiding internal data by making variables private
Acess Modifiers: -
                1)Public - self.name = name 
                2)Private - self.__name = name 
                3)Protect - self._name = name'''
class student:
    def __init__(self, sur, name, marks):
        self.sur = sur
        self._name = name
        self.__marks = marks
    def details(self):
        return f"{self.sur} {self._name} got {self.__marks} marks"
s1 = student("Kalagarla","Akhila",95)
s2 = student("Kalagarla","Nandu",98)
print(s1.details()) 
print(s1.sur)
print(s1._name)
print(s1._student__marks)


class student:
    def __init__(self):
        self.__name = ""
    def setname(self,n):
        self.__name = n 
    def getname(self):
        return self.__name 
obj = student()
obj.setname("Nandu")
print(obj.getname()) # Nandu