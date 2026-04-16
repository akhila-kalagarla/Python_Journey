# To check wether the given number is prime or not 
from sympy import prime


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True
n = int(input())
if is_prime(n):
    print(n, "is prime number")
else:
    print(n, "is not a prime number")
