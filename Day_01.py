"""
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]  
The problem requires us to count substrings that appear more than once. My solution involves creating a hash set to store all substrings and their counts. 
We then iterate over the elements and their counts stored in the hash set, appending the substring to the result list if its count is greater than 1.

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashSet = {}
        result = []
        for i in range(0 , len(s)-9):
            subString =s[i:i+10]
            if subString in hashSet:
                hashSet[subString] +=1
            else :
                hashSet[subString]=1
        for ele , count in hashSet.items():
            if count > 1:
                result.append(ele)
        return result
