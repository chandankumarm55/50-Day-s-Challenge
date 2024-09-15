class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        maxLength = 0
        length = len(s)
        for i in range(length):
            if length - i <= maxLength:
                break
            countA , countE, countI , countO, countU = 0,0,0,0,0
            currentSubstring =''
            for j in range(i,length):
                currentSubstring+=s[j]
                if s[j]=='a':
                    countA+=1
                elif s[j]=='e':
                    countE+=1
                elif s[j]=='i':
                    countI+=1
                elif s[j]=='o':
                    countO+=1
                elif s[j]=='u':
                    countU+=1
                if countA%2 ==0 and   countE%2 ==0 and  countI%2 ==0 and  countO%2 ==0 and countU%2 ==0:
                    maxLength = max(maxLength , len(currentSubstring))
        return maxLength
