class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        currentIndex  , count =0 , 0
        for val in nums :
            currentIndex+=val
            if currentIndex ==0:
                count+=1
        return count        
