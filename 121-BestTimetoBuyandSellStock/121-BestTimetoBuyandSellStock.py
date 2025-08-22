# Last updated: 8/21/2025, 7:34:37 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix loop
        n = len(nums)
        prefix = 1
        output = [0]*n
        
        for i in range(n):
            output[i] = prefix
            prefix = prefix*nums[i]
        
        #postfix
        postfix = 1
        for i in range(n-1,-1,-1):
            output[i]*=postfix
            postfix = postfix * nums[i]
        return output
        