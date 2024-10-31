class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLen = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                maxLen = max(maxLen, count)  
                count = 1
        
        maxLen = max(maxLen, count) 
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            else:
                maxLen = max(maxLen, count)  
                count = 1
        
        maxLen = max(maxLen, count) 
        return maxLen
