class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setArray = set(nums)
        listArray = list(setArray)
        if len(listArray) <= 2 :
            return listArray[-1]
        listArray.sort()
        reversedList = listArray[::-1]
        return reversedList[2]
