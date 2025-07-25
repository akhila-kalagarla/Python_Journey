'''Dictionaries - are denoted by key value pairs and every pair is separated by comma'''
phn = {"jhon":97048227682,"smith":98270456902,"akhila":9676455883}
print(phn["smith"]) # 98270456902

# Examples
a = {1:"a",2:"b",3:"c",4:"d"}
print(a.keys()) # dict_keys([1, 2, 3, 4])
print(a.values()) # dict_values(['a', 'b', 'c', 'd'])
print(a.items()) # dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
print(a[1]) # v
print(a.get(4)) # d
a.update({2:"e"})
print(a) # {1: 'a', 2: 'e', 3: 'c', 4: 'd'}
print(a.pop(4)) # d
print(a) # {1: 'a', 2: 'e', 3: 'c'}
print(a.popitem()) # (3, 'c')
print(a) # {1: 'a', 2: 'e'}
a.clear()
print(a) # {}

'''Example using user input'''
n = int(input())
dict = {}
for _ in range(n):
    k = input()
    v = input()
    dict[k] = v
print(dict) # {'1': 'akki', '2': 'nandu', '3': 'naya', '4': 'bharath'}
d1 = dict.copy()
print(d1)

'''To print the square numbers of a values'''
d = {1:2, 2:3, 3:4, 4:5}
for value in d.values():
    print(value**2,end = " ") # 4 9 16 25
'''Using user input'''
print()
n = int(input())
d = {}
for _ in range(n):
    k = int(input())
    v = int(input())
    d[k] = v*v
print(d.values()) # dict_values([1, 4, 9, 16])

'''Write a program to take a list of word and print the dictionary with the words as keys and the length of the words as values'''
n = list(map(str, input().split()))
d = {}
for word in n:
    if len(word) % 2 == 0:
        d[word] = len(word)
print(d) # {'akhila': 6, 'nandhu': 6, 'nayu': 4}
# Or
n = int(input())
arr = []
for i in range(n):
    a = input()
    arr.append(a)
print(arr) # ['akhila', 'nandhu', 'nayu']
d = {}
for i in arr:
    if len(i) % 2 == 0:
        d[i] = len(i)
print(d) # ['akhila', 'nandhu', 'nayu']
