class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxXor = 0
        maximumKvalue = 2 ** maximumBit - 1
        result = []
        for num in nums:
            maxXor ^= num
            print(maxXor)
            result.append(maximumKvalue ^ maxXor)
        
        return result[::-1]
