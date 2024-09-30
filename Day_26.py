class MyCalendarTwo(object):
    def __init__(self):
        self.bookings=[]
    def book(self, start, end):
        for prevStart , prevEnd in self.bookings:
            if start < prevEnd and end > prevStart:
                newStart = max(prevStart, start)
                newEnd = min(prevEnd , end)

                if self.check(newStart , newEnd):
                    return False
        self.bookings.append((start , end))
        return True

    def check(self , start ,end):
        overlapping = 0
        for prevStart , prevEnd in self.bookings :
            if prevStart < end and prevEnd > start:
                overlapping+=1
                if overlapping==2:
                    return True
        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
