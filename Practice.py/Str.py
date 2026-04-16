# To check given string is a palindrome or not 
def ispalindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return "palindrome"
    else:
        return "Not"
s = input()
print(ispalindrome(s))

# Recursive Two-Pointer Approach
def palin(s, left, right):
    if left >= right:
        return "Palindrome"
    if s[left] != s[right]:
        return "Not"
    return palin(s, left + 1, right - 1)
s = input()
print(palin(s, 0, len(s) - 1))


