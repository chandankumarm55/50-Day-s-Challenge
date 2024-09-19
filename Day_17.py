class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numsString = list(map(str , nums))
        def compare(array):
            length = len(array)
            for i in range(length):
                for j in range(0 , length-i-1):
                    if array[j]+array[j+1] < array[j+1]+array[j]:
                        array[j],array[j+1] = array[j+1],array[j]
        compare(numsString)
        result = "".join(numsString)
        return '0' if result[0] == '0' else result
