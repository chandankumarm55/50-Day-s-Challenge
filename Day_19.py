class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1format = str(num1).zfill(4)
        num2format = str(num2).zfill(4)
        num3format = str(num3).zfill(4)
        keyString= ''
        for i in range(4):
            currentString = min(num1format[i],num2format[i],num3format[i])
            keyString+=currentString
        return int(keyString)
  
