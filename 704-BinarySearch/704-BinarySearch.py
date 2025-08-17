# Last updated: 8/17/2025, 5:02:55 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        '''
        while start<=end:
            mid = int(start + (end-start)/2)
            if nums[mid] == target:
                return mid
            if nums[mid]> target:
                end = mid-1
            else:
                start = mid+1
        return -1
        '''

        #recursive
        return self.recursive_search(nums,target,start,end)

    def recursive_search(self,nums:List[int],target:int,start:int,end:int) -> int:
        mid = int(start+ (end-start)/2)
        if start>end:
            return -1
        if nums[mid] == target:
            return mid
        if target<nums[mid]:
            end = mid-1
        else:
            start = mid+1
        return self.recursive_search(nums,target,start,end)
