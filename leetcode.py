# '''1. '''
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

'''26.'''
class Solution:
    def removeduplicates(self, nums):
        if not nums:
            return 0 
        i = 0 
        for j in range(1, len(nums)):
            if nums[j] != nums[1]:
                i += 1 
                nums[i] = nums[j]
        return i + 1
nums=[1,1,2,3,3,4,4,5]
obj = Solution()
k = obj.removeduplicates(nums)
print(nums[:k])
