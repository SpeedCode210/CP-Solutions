# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def search(start = 0, prefix = "", count = 4):
            if count == 0:
                if start == len(s):
                    res.append(prefix[1:])
                return
            for end in range(start+1, min(start+4, len(s)+1)):
                K = int(s[start: end])
                if K <= 255 and K >= 0 and (s[start] != '0' or s[start: end] == '0'):
                    search(end, prefix + '.' + s[start: end], count - 1)

        search()
        return res