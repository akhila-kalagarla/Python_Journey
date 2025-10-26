#To remove special symbols from the given text
def process(text):
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    text = text.strip()
    return text
result = input("Enter a text:")   #Enter a text:###Hello i am Akhila from @Kiet-W with the roll no: 22JN1A4506,!
print(process(result)) #Output: Hello i am Akhila from KietW with the roll no 22JN1A4506

#To print a,c values
def num(a,b,c):
    print(a)
    #print(b)
    print(c)
    return [a,c]
a = int(input())
b = int(input())
c = int(input())
print(num(a,b,c)) #[a,c] values will be printed 

#Swapping of 2 variables
x = 5
y = 6
temp = x
x = y
y = temp
print(x)
print(y)
  #Or
x, y = y, x
print(x)
print(y)
  #Or
x = x + y
y = x - y
x = x - y
print(x)
print(y)

# #Expressions on the right-hand side are evaluated before assignment:
x = 100
y = "Akhila"

x, y = x - 1, y + "6"
print(x)
print(y)

# To check Truthy values
x = 7
if x:
  print(x,"is a number")

x = 0
if x:
   print(x,"is a number")

# Print the min or max numbers using ternary operator 
a, b = 10, 20 
min = a if a<b else b 
print(min) 
max = a if a>b else b 
print(max)

# Walrus operator example in python 3.8
num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())
print(num)
#
a = [{"id":1, "name":"Akhila", "age":20},
     {"id":2, "name":"Nandu", "age":19},
     {"id":3, "name":"Naya", "age":10}]
for i in a:
    if name:= i.get("name"):
        print(name)
print("Without walrus operator:")
for i in a:
    name = i.get("name")
    if name:
        print(name)