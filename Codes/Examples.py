# To append the elemnets in already intializes list
a = [1,2,3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4]
print(b) # [1, 2, 3, 4]
#OR
x = [1,2,3]
y = x[:]
y[0] = 100
print(x) # [1, 2, 3]

# It returns
print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')

n = int(input())
a, b = 0, 1
sum = 0
c = []
for i in range(n):
    print(a, end = ' ')
    a,b = b, a+b





