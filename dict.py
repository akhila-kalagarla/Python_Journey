'''Dictionaries - are denoted by key value pairs and every pair is separated by comma'''
phn = {"jhon":97048227682,"smith":98270456902,"akhila":9676455883}
print(phn["smith"]) # 98270456902

# Examples
a = {1:"a",2:"b",3:"c",4:"d"}
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


