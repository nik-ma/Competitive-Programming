class MyCalendar:

    def __init__(self):
        self.bookings=[]
        

    def book(self, start: int, end: int) -> bool:
        new=self.bookings[:]
        self.bookings.append([start,end])
        self.bookings.sort()
        i=1
        while i<len(self.bookings):
            if self.bookings[i][0]<self.bookings[i-1][1]:
                self.bookings=new
                return False
            i+=1
        return True
        
                


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)