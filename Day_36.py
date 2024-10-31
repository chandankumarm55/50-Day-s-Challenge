class Solution:
    def minLength(self, s: str) -> int:
        count = 0
        n = len(s)
        while True:
            if "AB" in s :
                s=s.replace('AB','')
            elif "CD" in s:
                s=s.replace('CD','')
            else:
                return len(s)
        
