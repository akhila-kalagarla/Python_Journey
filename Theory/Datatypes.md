### DATA TYPES
- *Variables can store data of different types and different types can do different things*
#### - *Text type*        :  str
#### - *Sequence types*   :  int, tuple, range
#### - *Mapping types*    :  Dictionary
#### - *Set type*         :  set,frozenset
#### - *Boolean type*     :  bool
#### - *Binary types*     :  Bytes, memory view, bytearray
#### - *None type*        :  none

### Type Conversion
- *We can convert the data type from one type to another type*
 ##### Ex:
     x = 1
     y = 2.8
     z = 1j
     a = float(x) #Output: 1.0
     b = int(y) #Output: 2
     c = complex(x) #Output: 1+0j
     d = float(x) #Output: 2.8

### Random Numbers
- *In python random() function is not there but, we have built-in modules in python called random. It is used to make a random numbers in a given range*
 ##### Ex:
     import random
     print(random.randrange(1,10)) #Output: 2
     - *The output will be any number in the given range from the given numbers*