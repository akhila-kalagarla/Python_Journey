# # Exception handling
# '''Handling the errors without getting any errors in output'''
# '''1.example on zerodivision error'''
# a = int(input())
# b = 0
# try:
#     c = a/b
# except ZeroDivisionError:
#     print("zero")
# '''2.To check your age is valid or not'''
# age = int(input("Enter your age:")) # 61
# try:
#     if age < 18:
#         raise ValueError;
#     else:
#         print("The age",age, "is valid") # The age 61 is valid
# except:
#     print("The age",age, "is not valid")