from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        needArray = []
        for  i in range(len(nums) - k+1):
            currentWindoweArray = nums[i:i+k]

            if len(set(currentWindoweArray)) != k or max(currentWindoweArray) - min(currentWindoweArray) !=k-1 :
                needArray.append(-1)
                continue 
            if sorted(currentWindoweArray) == currentWindoweArray :
                needArray.append(max(currentWindoweArray))
            else :
                needArray.append(-1)
        return needArray


        # for i in range(len(nums) - k + 1):
        #     currentWindowArray = nums[i:i + k]
        #     print(f"Current window: {currentWindowArray}")
            
        #     # Check if the elements are consecutive
        #     if len(set(currentWindowArray)) != k or max(currentWindowArray) - min(currentWindowArray) != k - 1:
        #         print("Elements are not consecutive")
        #         needArray.append(-1)
        #         continue
            
        #     # Check if the window is sorted
        #     if currentWindowArray == sorted(currentWindowArray):
        #         print("Window is sorted and consecutive")
        #         needArray.append(max(currentWindowArray))
        #     else:
        #         print("Window is not sorted")
        #         needArray.append(-1)
        
        # return needArray
