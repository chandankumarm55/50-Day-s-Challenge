class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxValue = max(nums)  #
        maxLen = 0
        currentLen= 0
        for num in nums:
            if num == maxValue:
                currentLen += 1
                maxLen = max(maxLen, currentLen) 
            else:
              
                currentLen = 0
        
        return maxLen
