# To append the elemnets in already intializes list
a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)
#OR
x = [1,2,3]
y = x[:]
y[0] = 100
print(x)

# It returns
print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')