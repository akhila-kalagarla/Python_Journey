# lst = [1,2,3,4]
# print(lst)
# print(type(lst))
# lst[0] = 0
# print(lst)

# list = [10,20,30,40,50]
# print(list[1:3:1])
# print(list[0:4:2])
# print(list[::-1])
# print(list[::-2])

# '''Append method'''
# lst = [10,20,30]
# lst.append(20) # [10, 20, 30, 20]
# lst.append([40,50]) # [10, 20, 30, 20, [40, 50]]
# print(lst)

# '''Extend method'''
# lst = [10,20,30]
# lst.extend([40,50,60]) # [10, 20, 30, 40, 50, 60]
# k = [70,80,90]
# lst.extend(k) # [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(lst)

# '''Insert method'''
# lst = [1,2,3,4,5]
# lst.insert(0,0)
# print(lst) # [0, 1, 2, 3, 4, 5]

# '''Remove method'''
# lst = [1,2,3,4,5]
# lst.remove(5)
# print(lst) # [1, 2, 3, 4]

# '''copy method'''
# lst = [1,2,3,4,5]
# a = lst.copy()
# print(a) # [1, 2, 3, 4, 5]

# '''pop method'''
# lst = [1,2,3,4,5]
# a = lst.pop() # # [1, 2, 3, 4]
# lst.pop(3) # [1, 2, 3]
# print(lst) 

'''count method'''
lst = [1,2,3,4,5,3,3,3]
a = lst.count(3) 
print(a) # 4