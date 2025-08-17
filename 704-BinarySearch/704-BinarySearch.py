# Last updated: 8/17/2025, 5:36:01 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #selection sort

        for i in range(len(nums)):
            min_i  = i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_i]:
                    min_i = j
            if min_i != i:
                nums[i],nums[min_i] = nums[min_i],nums[i]
               
        