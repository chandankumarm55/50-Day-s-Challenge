from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0
        i = 0
        while i < length:
            if  flowerbed[i]==0:
                isPrev = ( i==0 or flowerbed[i-1]==0 )
                isNext = ( i==length-1 or flowerbed[i+1]==0 )
                if isPrev and  isNext:
                    flowerbed[i]=1
                    count+=1
                    if count>=n:
                        return True
                    i+=1
            i+=1
        return count>=n
