#Functions
#Syntax
'''def function_name(parameters):
        #block of code
        return value  #(optional)'''

'''Term         -        Description
    def         -   keyword to define function
function_name   -   Any valid python identifier
  parameters    -   input passes to the function
     :          -   Ends the function header
indentend block -   code that runs when the fucntion is called
   return       -   Sends result back to caller '''

#Example:-
def hi():
    print("Hello students")
hi()    # Hello students
#Ex1:-
def students():
    return 80
total = students()
print("Total students :",total)  # Total students : 80
#Ex2-without using function calling:-
def stu():
    return 80
tot = stu()
print("Total students :",80) # Total students : 80

'''Function Arguments
3types of arguments
1.positional 2.Keyword 3.Default

#ex-on positional'''
def hi(name):
    print("hello",name)
hi("vijju")  # hello vijju

'''#ex- on Default'''
def hi(name="friends"):
    print("Hello",name)
hi()        # Hello friends
hi("Akki")  # Hello Akki

'''#ex- on Keyword'''
def stu(name,age):
    print("Name:",name)
    print("Age:",age)
stu(age = 19, name = "Akhila")  

'''------------------------------------------------------------------
   | Feature    |     Description               |    Example        |
   ------------------------------------------------------------------             
   |    def     |    defines a function        |   def hi()         |
   |  Arguments |    pass data into a function |   def hi(name):    |
   |   return   |    Sends result back         |   return a+b       |
   |    call    |    Use the function          |   Hi("Vijju")      | 
   ------------------------------------------------------------------ '''

#Types of functions:-
#examples:-
'''1.No Arguments, No return value'''
def fun():
    print("Keep smiling")
fun()   # Keep smiling
'''2.With Arguments, No Return value'''
def greet(name):
    print("Hello",name)
greet("students")  # Hello students
'''3.No Arguments, With Return value'''
def hi():
    return "friends"
value = hi()
print("Wishes:",value) # Wishes: friends
'''4.with Arguments and Return value'''
def add(a,b):
    return a+b
res = add(2,5)
print("Sum:",res)  #Sum: 7 

''' Day-7 - 10/07/2025 '''
# #Call by value
def modify(x):
    x = x+5
    print("Inside:",x)
a = 20
modify(a)
print("Outisde:",a)

#Call by reference
def item(list):
    list.append(5)
    print("Inside:",list)
num = [1,2,3,4]
item(num)
print("Outside:",num)

#Lambda function
'''syntax:-
lambda arguments:expression '''
#Ex:-
add = lambda a,b : a+b
print(add(9,3)) # 12
'''No arguments'''
greet = lambda:"HELLO!"
print(greet()) # HELLO!

'''lambda in a map() function'''
n = [1,2,3,4]
sq = list(map(lambda x : x**2, n))
print(*sq) # 1 4 9 16
'''Convert to uppercase'''
names = ['anu','vijju','gowthami']
up = list(map(str.upper,names))
print(up) #['ANU', 'VIJJU', 'GOWTHAMI']
