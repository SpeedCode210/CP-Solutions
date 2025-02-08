# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hi = defaultdict(int)
        for s in cpdomains:
            a = s.split()
            k = a[1].split(".")
            for i in range(len(k)):
                hi[".".join(k[i:])] += int(a[0])
        return [" ".join([str(hi[i]),i]) for i in hi]
            
        