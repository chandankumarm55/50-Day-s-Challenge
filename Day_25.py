class MyCalendar:
    def __init__(self):
        self.bookings = []
    def book(self, start: int, end: int) -> bool:
        for prevStart , prevEnd in self.bookings:
            if  start < prevEnd and end > prevStart:
                return False
        self.bookings.append([start,end])
        return True
    

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
