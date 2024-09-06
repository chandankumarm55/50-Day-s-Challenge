"""
The problem is to find the missing observations in dice rolls, where there are a total of n + m operations, but only m rolls are given, 
and the mean of all the rolls is provided. First, calculate the total sum using the mean and total operations. Then, find the missing sum by subtracting the 
sum of the given rolls from the total sum. Next, handle invalid cases where the missing sum is less than n (if all rolls were 1) or 
greater than 6 * n (if all rolls were 6). Finally, distribute the missing sum across n dice rolls by first assigning a base value to each roll and then
distributing any remainder evenly by adding 1 to some elements.
 
"""
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        totalSum = mean*(len(rolls)+n)
        missingSum = totalSum - sum(rolls)
        print(missingSum)

        if missingSum < n or missingSum > 6*n:
            return []
        baseValue = missingSum//n
        missingArray = [baseValue]*n
        remaining = missingSum%n
        for i in range(remaining):
            missingArray[i]+=1
        return missingArray
