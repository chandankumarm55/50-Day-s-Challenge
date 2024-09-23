class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minCount = [ele for ele in nums if ele < k]
        return len(minCount)
        
