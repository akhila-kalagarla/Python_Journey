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

class employee:
    def __init__(self,empid, name, salary, depart):
        self.emipd = empid 
        self.__name = name 
        self.__salary = salary 
        self._depart = depart 
    def setsalary(self, sal):
        if sal > 0:
            self.__salary = sal 
        else:
            print("Invalid")
    def getsalary(self):
        return self.__salary 
    def setname(self, namee):
        if namee.strip() != "":
            self.__name = namee 
        else:
            print("Name cannot be empty")
    def getname(self):
        return self.__name 
    def display(self):
        print("\n\tEmployee Details")
        print(f"Employee id        :{self.emipd}")
        print(f"Employee Name      :{self.__name}")
        print(f"Department         :{self._depart}")
        print(f"Employee salary    :{self.__salary}")
emp1 = employee(101,"Hemanth",95000,"AI Research") 
print("\n\tEmployee Details")
print("Employee id        :",emp1.emipd)
print("Employee Name      :",emp1.getname())
print("Department         :",emp1._depart)
print("Employee salary    :",emp1.getsalary())
emp1.setname("Hemanth sir")
emp1.setsalary(100000)
emp1.setname(" ")
emp1.display()