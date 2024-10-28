class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1)==1 :
            if s1 in s2 :
                return True
        s1Counter = Counter(s1)
        for i in range(0, len(s2)- len(s1)+1):
            currentWindowCount= Counter(s2[i:i+len(s1)])
            print(currentWindowCount)
            if currentWindowCount == s1Counter:
                return True
        return False
