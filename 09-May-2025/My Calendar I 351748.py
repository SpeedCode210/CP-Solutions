# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.data = [-1, 10**9+2]

    def book(self, startTime: int, endTime: int) -> bool:
        endTime -= 1
        a = 0
        b = len(self.data) - 1

        while a < b:
            m = (a+b+1)//2
            if self.data[m] < startTime:
                a = m
            else:
                b = m-1
        if a%2 == 1 or self.data[a+1] <= endTime:
            return False

        self.data = self.data[:a+1] + [startTime, endTime] + self.data[a+1:]
        
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)