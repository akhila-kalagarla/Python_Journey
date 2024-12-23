## VARIABLES INTRO
- *Variables are created to assign a values*
 ##### Ex:
    x = 5
    print(x) #output: 5
    x = "Akhila"
    print(x) #output: Akhila

### Creating variables
- *Python has no command to declare variables*
- *A variable is created when we assign a value*
- *Variables can't change be declared with a particular type, we can change value after it has to set*

### Casting of a variable
- *If we want to specify a data type of a variable, then it can be done with casting*
 ##### Ex:
    x = str(3) #output: 3
    y = int(3) #output: 3
    z = float(3) #output: 3.0

#### To get variable type
- *By using type() function we can get the variable type
 ##### Ex:
    x = "Akhila"
    y = 5
    print(type(x)) #output: <class 'str'>
    print(type(y)) #output: <class 'int'>

### Variable names
###### Rules of python variables
- *A variable must be start with a alphabet or underscore(_)*
- *A variable name cannot be start with a numeric number*
- *A variables name can have only aplhanumeric & underscore symbols (A-Z),(0-9) and "_"*
- *Variables are case-sensitive (age,Age,AGE are not same)
- *A variables name cannot be any python keywords*
 ##### Ex:
    myvar = " "
    my_var = " "
    _myvar = " "
    my_var2234 = " "
    my2_var = " "

### Multi word variable names
- *Variabes are more than one word are different to read
- *so for this we have 3cases for readability
            - *Camel Case*
            - *Pascal Case*
            - *Snake Case*
###### Camel Case:
- *In this case each word starts with a capital letters except first word
 ##### Ex:
     myVariableName = "Akhila"
###### Pascal Case:
- *In this case each and every word starts with a capital letter*
 ##### Ex:
     MyVariableName = "Akhila"
###### Snake Case: 
- *In this case every word is separated by underscore*
 ##### Ex:
     my_Variable_name = "Akhila"

### Variables are case-sensitive
 ##### Ex:
     a = 5
     A = "Akhila"
     print(a) # A will not overwrite the a #output: 5

### Assign multiple values
- *We can assign multiple values to multiple variables or we can assign single values to multiple variables
 ##### Ex:
     x,y,z = "orange","banana","mango"
     print(x) #output: orange
     print(y) #output: banana
     print(z) #output: mango
 ##### Ex:
     x = y = z = "orange"
     print(x,y,z) #Output: orange orange orange      

### Unpack a collection
- *If we have a collection of values in a list,tuple, etc.. python allows us to extract the values into variables. This is called Unpacking*
 ##### Ex:
     fruits = ["apple","banana","cherry"]
     x,y,z = fruits
     print(x) #output: apple
     print(y) #output: banana
     print(z) #output: cherry

### Output variables
- *The python print() function is often used to output variables*
 ##### Ex:
     x = "python"
     y = "is"
     z = "awesome"
     print(x, y, z) #Output: python is awesome
     print(x + y + z) #Output: python is awesome
 ##### Ex:
     x = 5
     y = 10
     print(x + y) #Output: 15

### Global variables
- *Global variables are created outside of a function*
 ##### Ex:
     x = "awesome"
     def myfunc():
         print("python is" +x) #Output: python is awesome
     myfunc()
- *If a variable is declared inside of the function then the variable is only in that block of function.*
- *If we assign a variable outside of the function we use that variable throughout the program.*
 ##### Ex:
     x = "awesome"
     def myfunc():
         x = "fantastic"
         print("python is", x) #Output: python is fantastic
     myfunc()
     print("python is", x) #Output: python is awesome
### Global keyword
 ##### Ex:
     def myfunc():
        global x
        x = "fantastic"
     myfunc()
     print("python is" +x) #Output: python is fantastic
 ##### Ex:   
     x = "awesome"
     def myfunc():
        global x 
        x = "easy to understand"
     myfunc()
     print("python is" +x)  #Output: python is easy to understand
     


