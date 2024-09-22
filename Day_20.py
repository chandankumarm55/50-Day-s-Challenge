class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        string = str(x)
        total = 0
        for ele in string:
            total+=int(ele)
        if x%total == 0 :
            return total
        else :
             return -1
