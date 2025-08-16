# Last updated: 8/15/2025, 7:50:02 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        num = {key:0 for key in range(len(nums)+1)}
        for i in nums:
            num[i]+=1
        for key,val in num.items():
            if val == 0:
                return key
        '''

        #optimal
        n = len(nums)
        return ((n*(n+1))//2)-sum(nums)

        