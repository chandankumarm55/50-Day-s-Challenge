class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR of start and goal will give bits that differ
        xor = start ^ goal
        print(start , goal , xor)
        # Count the number of 1s in the binary representation of xor
        return bin(xor).count('1')
