###Numeric data types
a = 10
print(a) #10
a = 10
print(type(a)) #<class 'int'>
a = 10.5
print(a) #10.5
print(type(a)) #<class 'float'>
a = 5+3j
print(a) #(5+3j)
print(type(a)) #<class 'complex'>

###Text data type
name = 'Akhila' 
quote = "old is gold"
multi = '''This is a multi line string'''
print(name) #Akhila
print(quote) #old is gold
print(multi) #This is a multi line string
print(type(name)) #<class 'str'>
print(type(quote)) #<class 'str'>
print(type(multi)) #<class 'str'>

###Set data types - Unorderd,{},Unique
set = {1,2,5,2,4}
print(set) #{1, 2, 4, 5}

###Boolean data type
a = 2
print(bool(a)) #True
a = []
print(bool(a)) #False

###Sequence data types
#LIST - [],Mutable,Ordered
list = [10,20,"kiet",30]
print(list) #[10, 20, 'kiet', 30]
print(list[0]) #10
list[0] = 80
print(list) #[80, 20, 'kiet', 30]
#TUPLES - (),Ordered, Immutable
tup = (10,20,"kiet",50)
print(tup) #(10, 20, 'kiet', 50)

###Mapping data type
#Dictionary - {}, keys:values, keys-immutable, values-mutable
dict = {"name":"Akhila","age":42}
print(dict) #{'name': 'Akhila', 'age': 42}
print(dict.values()) #dict_values(['Akhila', 42])
print(dict.keys()) #dict_keys(['name', 'age'])
print(dict.items()) #dict_items([('name', 'Akhila'), ('age', 42)])

###Inputs and Outputs
#####Inputs
#To take int as input
a = int(input("Enter a number:")) #Enter a number:6
b = int(input("Enter a number:")) #Enter a number:7
print(a) #6
print(b) #7
print(a+b) #13
#To take string as input
name = input("Enter your name: ") #Enter your name: Akhila
print("Hi", name) #Hi Akhila
#To take multiple inputs in one line
x, y = input("Enter two numbers separated by space: ").split() #6 9
print(x) #6
print(y) #9
print(x, y) #7 8

#####Outputs
#Simple output
print("Hello, World!")
print("Welcome","to","python","language", sep = "-")
print("Loading", end = "...")

#Comments
#####Single line comment
#starts with # symbol
print("hi")#This msg not print #hi
#####Multi line comment
'''This is multi line  comment python ignores this multi line comments'''

