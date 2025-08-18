# Last updated: 8/18/2025, 6:23:14 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L = 0
        R = n-1
        
        while L<= R:
            total = numbers[L]+numbers[R]
            if total == target:
                return [L+1,R+1]
            if total> target:
                R-=1
            else:
                L+=1