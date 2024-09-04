"""
Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

The problem is to first convert each character to its index based on its position in the alphabet. For example, 
if the character is 'a', then it will be 1, and if it's 'z', it will be 26, and so on. After that, we have k operations to perform. 
In each operation, we calculate the sum of the digits in the string obtained from the previous step. We repeat this operation k times. 
Finally, we need to return the remaining number as an integer.

Time Complexity: O(n + k * m)
Space Complexity: O(n)

"""
class Solution:
    def getLucky(self, s, k) :
        result=""
        for ele in s:
            currentNumber = ord(ele) - 96
            result+=str(currentNumber)
        ans = ''
        print(result)
        for _ in range(k):
            currentNumber=0
            for i in range(len(result)):
                currentNumber+= int(result[i])
            result = str(currentNumber)
        return int(result)
