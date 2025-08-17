# Last updated: 8/17/2025, 4:32:09 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = int(start + (end-start)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]> target:
                end = mid-1
            else:
                start = start+1
        return -1