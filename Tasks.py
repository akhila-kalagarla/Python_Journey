#Write a python program to find min and max values without using min,max methods
arr = [2,8,10,28,19,0]
value = val = arr[0]
for i in arr:
    if i > value:
        value = i
    if i < val:
        val = i
print(value)
print(val)
#Or
l = [4,7,9,10,32,75,20]
s = l.sort()
min = l[0]
max = l[-1]
print(min,max)


