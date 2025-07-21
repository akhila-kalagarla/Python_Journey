a = [1,2,3]
b = a
b.append(4)
print(a)
print(b)

x = [1,2,3]
y = x[:]
y[0] = 100
print(x)