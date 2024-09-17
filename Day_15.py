class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinitues(time):
            hours , minitues = map(int, time.split(':'))
            totalMinitues = hours*60 +  minitues
            return totalMinitues
        convertedTOMinitues = [convertToMinitues(time) for time in timePoints]
        convertedTOMinitues.sort()
        print(convertedTOMinitues)
        minDiffernce = float('inf')
        
        for i in range(1,len(convertedTOMinitues)):
            minDiffernce = min(minDiffernce , convertedTOMinitues[i]-convertedTOMinitues[i-1])
        
        #handling the 24 hour circle
        minDiffernce = min(minDiffernce ,1440 + convertedTOMinitues[0] - convertedTOMinitues[-1])

        return minDiffernce
