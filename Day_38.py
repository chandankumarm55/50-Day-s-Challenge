class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        fristRow = set('qwertyuiop')
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        array = []
        for ele in words:
            low_ele =ele.lower()
            result1 = all(char in fristRow for char in low_ele)
            result2 = all(char in secondRow for char in low_ele)
            result3 = all(char in thirdRow for char in low_ele)
            if result1 or result2 or result3 :
                array.append(ele)
        return array
