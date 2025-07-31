# # To append the elemnets in already intializes list
# a = [1,2,3]
# b = a
# b.append(4)
# print(a) # [1, 2, 3, 4]
# print(b) # [1, 2, 3, 4]
# #OR
# x = [1,2,3]
# y = x[:]
# y[0] = 100
# print(x) # [1, 2, 3]

# # It returns
# print(tuple("hello")) # ('h', 'e', 'l', 'l', 'o')

# n = int(input())
# a, b = 0, 1
# sum = 0
# c = []
# for i in range(n):
#     print(a, end = ' ')
#     a,b = b, a+b

# '''To remove special symbols and extra spces in a given string'''
# n = input()
# r = ''
# for i in n:
#    if i.isalnum() or i.isspace:
#       r += i
# print(r)

n = list(map(int, input().split()))
f = s = float('-inf')
for i in n:
    if i > f:
        s = f
        f = i
    elif i > s and i != f:
        s = i
if s == float('-inf'):
    print("No second largest element")
else:
    print(s)

   
   
      


