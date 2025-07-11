# Recursion
def x(n):
    if n == 0:
        print("Hello off")
        return
    print(n, end = ",")
    x(n-1)
x(5)

#Ex2:-
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

print(fact(1)) # 24
