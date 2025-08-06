'''1. '''
'''2. To print the product of elements in the given array except the self element(problem 238 in LeetCode)'''
nums = [1,2,3,4]
n = len(nums)
op = [1]*n
prefix = 1
for i in range(n):
    op[i] = prefix
    prefix *= nums[i]
suffix = 1
for i in range(n -1, -1, -1):
    op[i] *= suffix
    suffix *= nums[i]
print(op) # [24, 12, 8, 6]
