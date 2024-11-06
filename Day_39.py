class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        result = ""

        while i < n:
            count = 1
            while i + count < n and word[i+count ] == word[i] and count < 9:
                count+=1
            result+=str(count)+ word[i]
            i +=count
        return result
        
       
