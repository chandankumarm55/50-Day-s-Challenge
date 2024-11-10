class Solution(object):
    def canSortArray(self, nums):
        sortedNums = sorted(nums)
        if nums == sortedNums:
            return True
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                binOfj = bin(nums[j]).count('1')
                binOfNext = bin(nums[j + 1]).count('1')
                if nums[j] > nums[j+1] and binOfj == binOfNext:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
            if nums == sortedNums:
                return True
       
        return nums == sortedNums
