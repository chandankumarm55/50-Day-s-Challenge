from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedUnique = sorted(set(arr))

        sortedRank ={val:idx+1 for idx,val in enumerate(sortedUnique)}

        return [sortedRank[num] for num in arr]
