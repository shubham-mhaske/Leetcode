# Last updated: 8/15/2025, 7:52:34 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) != 2:
                return i