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
#Range

###Mapping data type
#Dictionary - {},
