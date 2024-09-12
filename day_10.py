class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for element in words:
            isCount = True
            for ele in element:
                if  ele not in allowed :
                    isCount = False
                    break
            if isCount:
                count+=1
        return count
