#Functions
#Syntax
'''def function_name(parameters):
        #block of code
        return value  #(optional)'''

'''Term        -        Description
    def        -   keyword to define function
function_name  -   Any valid python identifier
  parameters   -   input passes to the function
     :         -   Ends the function header
indentend block-   code that runs when the fucntion is called
   return      -   Sends result back to caller '''

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