class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        value = 1
        for ele in columnTitle:
            count = count*26 + (ord(ele) - ord('A') + 1)
        return count
