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
'''#ex- on Default '''
def hi(name="friends"):
    print("Hello",name)
hi()        # Hello friends
hi("Akki")  # Hello Akki