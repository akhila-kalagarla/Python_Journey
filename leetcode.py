#Leet code problems
'''238 - Problem in Leet code. To print the product of elements in the given array except the self element'''
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

'''26 - Problem in Leet code. To remove duplicates from the sorted array and return the new length of the array'''
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
print(nums[:k]) # [1, 2, 3, 4, 5]

'''3136 - To check the given string is valid or not by using regular expressions'''
import re
class Solution:
    def isvalid(self, word:str) -> bool:
        return bool(re.fullmatch(r'(?i)(?=.[aeiou])(?=bcdfghjklmnpqrstvwxyz])[a-z0-9]{3,}', word))
word = "abc12"
obj = Solution()    
print(obj.isvalid(word))  # True


