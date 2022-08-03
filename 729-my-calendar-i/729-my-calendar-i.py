class MyCalendar:
    def __init__(self):
        self.arr = []
        
    def book(self, start, end):
        q1 = bisect_right(self.arr, start)
        q2 = bisect_left(self.arr, end)
        if q1 == q2 and q1 % 2 == 0:
            self.arr[q1:q1] = [start, end]
            return True
        return False
                


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)