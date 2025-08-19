# String opearations module
def reverse_string(s):
    return s[::-1]
def to_uppercase(s):
    return s.upper()
def to_lowercase(s):
    return s.lower()
def capitalize_string(s):
    return s.capitalize()
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')