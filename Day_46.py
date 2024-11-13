from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binarySearch(left, right, target):
            while left <= right:
                m = (left + right) // 2
                if nums[m] > target:
                    right = m - 1
                else:
                    left = m + 1
            print(right)
            return right
        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (
                binarySearch(i + 1, len(nums) - 1, up) 
                - binarySearch(i + 1, len(nums) - 1, low - 1)
            )
        
        return res
