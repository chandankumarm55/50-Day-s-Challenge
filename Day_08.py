class Solution(object):
    def mySqrt(self, x):
        if x < 2:  # Handle small cases
            return x
        start = 1
        end = x // 2
        
        while start <= end:
            mid = (start + end) // 2  # Fix assignment here
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        
        return end  
