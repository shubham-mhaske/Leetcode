# Last updated: 8/15/2025, 7:52:38 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if  diff in pos:
                return [pos[diff],i]
            else:
                pos[nums[i]] = i 