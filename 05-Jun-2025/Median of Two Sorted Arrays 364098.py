# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findFirstBigger(self,target: int, nums : List[int]):
        a = 0
        b = len(nums)
        while b > a:
            m = (a+b)//2
            if nums[m] <= target:
                a = m+1
            else:
                b = m
        return b
    def findFirstLess(self,target: int, nums : List[int]):
        a = -1
        b = len(nums)-1
        while b > a:
            m = (a+b+1)//2
            if nums[m] >= target:
                b = m-1
            else:
                a = m
        return b

    def findRightMedian(self, nums1: List[int], nums2: List[int]) -> float:
        targetIndex = (len(nums1)+len(nums2))//2
        a = 0
        b = len(nums2)-1

        while b >= a:
            m = (a+b)//2
            X = self.findFirstLess(nums2[m], nums1) + 1 + m
            Y = self.findFirstBigger(nums2[m], nums1) + m
            if X > targetIndex:
                b = m-1
            elif Y < targetIndex:
                a = m+1
            else:
                print(X,targetIndex,Y)
                return nums2[m]

        return self.findRightMedian(nums2, nums1)

    def findLeftMedian(self, nums1: List[int], nums2: List[int]) -> float:
        targetIndex = (len(nums1)+len(nums2)-1)//2
        a = 0
        b = len(nums2)-1

        while b >= a:
            m = (a+b)//2
            X = self.findFirstLess(nums2[m], nums1) + 1 + m
            Y = self.findFirstBigger(nums2[m], nums1) + m
            if X > targetIndex:
                b = m-1
            elif Y < targetIndex:
                a = m+1
            else:
                return nums2[m]

        return self.findLeftMedian(nums2, nums1)




    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) == 0:
            return nums1[len(nums1)//2] if len(nums1)%2 == 1 else (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2
        if len(nums1) == 0:
            return nums2[len(nums2)//2] if len(nums2)%2 == 1 else (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2

        return (self.findLeftMedian(nums1, nums2)+self.findRightMedian(nums1, nums2))/2

        

