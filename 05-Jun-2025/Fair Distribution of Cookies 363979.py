# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def hi(self, i : int, maxi):
        if i == len(self.cookies):
            self.res = maxi
            return
        for j in range(self.k):
            self.children[j] += self.cookies[i]
            if self.children[j] < self.res :
                self.hi(i+1, max(self.children[j], maxi))
            self.children[j] -= self.cookies[i]

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.children = [0]*k
        self.res = 1000000000
        self.cookies = cookies
        self.k = k
        self.hi(0, 0)
        return self.res