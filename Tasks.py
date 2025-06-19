#Write a python program to find min and max values without using min,max methods
arr = [2,8,10,28,19,0]
value = arr[0]
for i in arr:
    if i > value:
        value = i
print(value)

           #OR

arr = [4,9,2,7,6,1,21]
s = l = arr[0]
for i in arr:
    if i < s:
        s = i
    if i > l:
        l = i
print(s)
print(l)