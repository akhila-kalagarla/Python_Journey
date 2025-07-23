lst = [1,2,3,4]
print(lst) # [1, 2, 3, 4]
print(type(lst)) # <class 'list'>
lst[0] = 0
print(lst) # [0, 2, 3, 4]

'''List slicing'''
list = [10,20,30,40,50]
print(list[1:3:1]) # [20, 30]
print(list[0:4:2]) # [10, 30]
print(list[::-1]) # [50, 40, 30, 20, 10]
print(list[::-2]) # [50, 30, 10]

'''List methods'''

'''Append method'''
lst = [10,20,30]
lst.append(20) # [10, 20, 30, 20]
lst.append([40,50]) # [10, 20, 30, 20, [40, 50]]
print(lst)
'''Extend method'''
lst = [10,20,30]
lst.extend([40,50,60]) # [10, 20, 30, 40, 50, 60]
k = [70,80,90]
lst.extend(k) # [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(lst)
'''Insert method'''
lst = [1,2,3,4,5]
lst.insert(0,0)
print(lst) # [0, 1, 2, 3, 4, 5]
'''Remove method'''
lst = [1,2,3,4,5]
lst.remove(5)
print(lst) # [1, 2, 3, 4]
'''copy method'''
lst = [1,2,3,4,5]
a = lst.copy()
print(a) # [1, 2, 3, 4, 5]
'''pop method'''
lst = [1,2,3,4,5]
a = lst.pop() # # [1, 2, 3, 4]
lst.pop(3) # [1, 2, 3]
print(lst) 
'''count method'''
lst = [1,2,3,4,5,3,3,3]
a = lst.count(3) 
print(a) # 4
'''index method'''
lst = [1,2,3,4,5,3,3,3]
a = lst.index(4) 
print(a)  # 3
'''clear'''
lst = [1,2,3,4,5,3,3,3]
lst.clear()
print(lst) # []
'''sort method'''
lst = [1,4,2,3,5]
lst.sort()
print(lst) # [1, 2, 3, 4, 5]
print(*lst) # 1 2 3 4 5
lst = [1,4,2,3,5]
lst.sort(reverse=True)
print(lst) # [5, 4, 3, 2, 1]
'''reverse method'''
lst = [10,20,30,40]
lst.reverse()
print(lst) # [40, 30, 20, 10]


# '''Date:- 23/07/25 Wednesday'''
### list comprehension
'''To print square of the numbers'''
n = int(input())
s = [x**2 for x in range(n)]
print(s) # [0, 1, 4, 9, 16]
# OR
n = list(map(int, input().split())) # 1 2 3 4 5 6 7
s = [x**2 for x in n]
print(s) # [1, 4, 9, 16, 25, 36, 49]
'''To print even numbers'''
even = [x for x in range(10) if x %2 == 0]
print(even) # [0, 2, 4, 6, 8]
# OR
n = list(map(int, input().split())) # 1 2 3 4 5 6 7 8 9 10
even = [x for x in n if x %2 == 0]
print(even)  # [2, 4, 6, 8, 10]
'''To print even or odd'''
i = list(map(int, input().split())) # 1 2 3 4 5 6 7 8 9 10
n = ["even" if x%2==0 else "odd" for x in i]
print(n) # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
# OR
n = ["even" if x%2==0 else "odd" for x in range(10)]
print(n) # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']

