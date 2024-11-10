class Solution(object):
    def minimumCost(self, nums):
        sum = nums[0]
        nums = nums[1:]
        nums.sort()
        return sum + nums[0] + nums[1] 
        
        
