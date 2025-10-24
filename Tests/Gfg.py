# #To remove special symbols from the given text
# def process(text):
#     text = ''.join(e for e in text if e.isalnum() or e.isspace())
#     text = text.strip()
#     return text
# result = input("Enter a text:")   #Enter a text:###Hello i am Akhila from @Kiet-W with the roll no: 22JN1A4506,!
# print(process(result)) #Output: Hello i am Akhila from KietW with the roll no 22JN1A4506

# #To print a,c values
# def num(a,b,c):
#     print(a)
#     #print(b)
#     print(c)
#     return [a,c]
# a = int(input())
# b = int(input())
# c = int(input())
# print(num(a,b,c))

# #Swapping of 2 variables
# x = 5
# y = 6
# temp = x
# x = y
# y = temp
# print(x)
# print(y)
#   #Or
# x, y = y, x
# print(x)
# print(y)
#   #Or
# x = x + y
# y = x - y
# x = x - y
# print(x)
# print(y)


# #Expressions on the right-hand side are evaluated before assignment:
x = 100
y = "Akhila"

x, y = x - 1, y + "6"
print(x)
print(y)

