# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def merge_sort(self, begin: int, end: int):
        middle = (begin+end)//2
        if begin != end:
            self.merge_sort(begin, middle)
            self.merge_sort(1+middle,end)
        p1 = begin
        p2 = middle+1
        for i in range(begin, end+1):
            if p1 > middle:
                self.cache[i] = self.nums[p2]
                p2+=1
            elif p2 > end:
                self.cache[i] = self.nums[p1]
                p1+=1
            else:
                if self.nums[p1] < self.nums[p2]:
                    self.cache[i] = self.nums[p1]
                    p1+=1
                else:
                    self.cache[i] = self.nums[p2]
                    p2+=1
        for i in range(begin, end+1):
            self.nums[i] = self.cache[i]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.cache = nums.copy()
        self.merge_sort(0, len(nums)-1)
        return self.nums