class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest = []
        score = []
        for i ,ele in enumerate(mat) :
            score.append((i,sum(ele)))
        print(score)
        sortedOne = sorted(score , key=lambda x:x[1])
        print(sortedOne)
        for ele in sortedOne:
            print(ele)
            if len(weakest) >= k :
                break
            weakest.append(ele[0])
        return weakest
        
        
        
