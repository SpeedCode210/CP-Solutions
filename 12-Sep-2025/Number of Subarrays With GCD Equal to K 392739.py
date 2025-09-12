# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            if a < b:
                a,b = b,a
            if b == 0:
                return a
            return gcd(b, a%b)
        res = 0

        n = len(nums)
        segtree = [0 for i in range((4*len(nums)))]

        def build(i, b,e):
            nonlocal segtree
            nonlocal nums
            if b == e:
                segtree[i] = nums[b]
                return
            build(i*2+1, b, (b+e)//2)
            build(i*2+2, (b+e)//2+1, e)
            segtree[i] = gcd(segtree[i*2+1], segtree[i*2+2])
        
        def get(i,b,e,l,r):
            if b == l and e == r:
                return segtree[i]
            if l > (b+e)//2:
                return get(2*i+2, (b+e)//2+1, e, l,r)
            if r <= (b+e)//2:
                return get(2*i+1,b, (b+e)//2, l,r)
            return gcd(get(2*i+2, (b+e)//2+1, e, (b+e)//2+1,r), get(2*i+1,b, (b+e)//2, l,(b+e)//2))
        
        build(0,0,len(nums)-1)

        for i in range(len(nums)):
            if nums[i] < k or get(0,0,n-1,i,n-1) > k:
                continue

            a = i
            b = len(nums)-1
            while a < b:
                m = (a+b)//2
                g = get(0,0,n-1,i, m)
                if g <= k:
                    b = m
                else:
                    a = m+1
            beg = a

            a = i
            b = len(nums)-1

            if get(0,0,n-1,i,n-1) == k:
                a = n
               
            while a < b:
                m = (a+b)//2
                g = get(0,0,n-1,i, m)
                if g < k:
                    b = m
                else:
                    a = m+1

            res += a-beg

        return res