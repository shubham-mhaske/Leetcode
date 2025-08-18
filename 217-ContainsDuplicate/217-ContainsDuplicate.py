# Last updated: 8/18/2025, 1:54:27 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #merge sort
        nums = self.merge_sort(nums)
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    

    def merge_sort(self,arr):
        n = len(arr)
        if n <=1:
            return arr
        
        m = n //2
        L = arr[:m]
        R = arr[m:]
        L = self.merge_sort(L)
        R = self.merge_sort(R)

        sorted_arr= [0]*n
        #conquer
        l_len = len(L)
        r_len = len(R)
        i,l,r = 0,0,0

        while l<l_len and r< r_len:
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l+=1
            else:
                sorted_arr[i] = R[r]
                r+=1
            i+=1
        while l<l_len:
            sorted_arr[i] = L[l]
            l+=1
            i+=1
        while r<r_len:
            sorted_arr[i] = R[r]
            r+=1
            i+=1
        return sorted_arr


