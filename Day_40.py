class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        splited = sentence.split(' ')
        if splited[0][0] != splited[-1][-1]:
            return False
        print(splited)
        for i in range(len(splited)-1):
            if splited[i][-1] != splited[i+1][0]:
                return False
        return True
