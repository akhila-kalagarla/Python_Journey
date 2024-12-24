### STRINGS
- *Strings in python are declared by using single quotes or double quotes.*
 ##### Ex:
    print("Hello") #Output: Hello
    print('Hello") #Output: Hello

##### Quotes inside the quotes
 ##### Ex:
     print("It's alright") #Output: It's alright
     print("I am 'Akhila'") #Output: I am 'Akhila'

### Strings are arrays
- *In strings we use square brackets[] to access elements of a string
 ##### Ex:
    a = "Akhila"
    print(a[0]) #Output: A
    print(a[3]) #Output: i
    print(a[2]) #Output: h

### Looping through a string
- *Since strings are arrays, we use loop through the characters in a string, with a for loop*
 ##### Ex:
     for x in range "Akhila":
        print(x, end=" ") #Output: A k h i l a
        print(x, end=",") #Output: A,k,h,i,l,a
        print(x)  #Output: A
                           k
                           h
                           i
                           l
                           a

### String Slicing
- *We can return a string characters in a range by using slice syntax*
- *Start index and end index is separated by colon*
 ##### Ex:
     a = "Akhila"
     print(a[1:3]) #Output: kh
     print(a[:3]) #Output: Akh
     print(a[3:]) #Output: ila
### Negative indexing
- *Negative indexing is used to access the elements from the backward*
 ##### Ex:
     a = "Akhila"
     print(a[-4:-2]) #Output: hil
### Modify strings
- *We can also modify the python strings once they already declared by using string methods*
### String Concatenation
- *we can combine the two values by using the concatenation when we assign to the variables*
 ##### Ex:
     x = "Hello"
     y = "world"
     print(x+y) #Output: Helloworld
     print(x+" "+y) #Output: Hello world

### String format
- *We cannot combine strings and numbers*
- *By using F-strings we can combine strings & numbers.*
 ##### Ex:
     age = 19
     txt = f"I am Akhila, my age is {age}"
     print(txt) #Output: I am Akhila, my age is 19

### Placeholder
- *A placeholder can include a modifier to format the value, we include ':' and .2f*
- *Here 2 represents the decimals*
 ##### Ex:
     price = 29
     txt = f"My shoes tag number is {price:.2f}"
     print(txt) #Output: My shoes tag number is 29.00
- *Here placeholder can contain python code, like math operations*
 ##### Ex:
     txt = f"My marks are {7*9} in each subject"
     print(txt) #Output: My marks are 63 in each subject

### Escape Character
- *An escape character is a backslash '\' followed by the character you want to insert*
 ##### Ex:
     txt = "I am Akhila \"Indian"\ from Global Coding Club"
     print(txt) #Output: I am Akhila "Indian" from Global Coding Club

- *There are some escape characters in python*
 ##### \\' - Single quote
 ##### \\\ - It inserts single slash where ever you want
 ##### \n - It uses to get new line
 ##### \r - Carriage return
 ##### \t - It uses for tab
 ##### \b - It uses for backspace
 ##### \f - It uses for form feed
 ##### \000 - It used for octal value
 ##### \xhh - It used for hex value