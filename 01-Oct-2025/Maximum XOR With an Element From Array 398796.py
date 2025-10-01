# Problem: Maximum XOR With an Element From Array - https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/

class Node:
    def __init__(self):
        self.children = [None, None]


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        self.root = Node()

        def insert(n):
            curr = self.root
            for i in range(31, -1, -1):
                bit = (n>>i)&1
                if curr.children[bit] is None:
                    curr.children[bit] = Node()
                curr = curr.children[bit]

        def maximize_xor(n):
            curr = self.root
            if curr.children[0] is None and  curr.children[1] is None:
                return -1
            res = 0
            for i in range(31, -1, -1):
                bit = 1 - ((n>>i)&1)
                res += (1<<i)
                if curr.children[bit] is None:
                    bit = 1 - bit
                    res -= (1<<i)
                curr = curr.children[bit]
            return res

        nums.sort()
        p = 0

        resu = [0]*len(queries)
        queries = [[x[0],x[1],i] for i,x in enumerate(queries)]
        queries.sort(key = lambda x : x[1])
        for q in queries : 
            while p < len(nums) and nums[p] <= q[1]:
                insert(nums[p])
                p += 1
            resu[q[2]] = maximize_xor(q[0])


        return resu
