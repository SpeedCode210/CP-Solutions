# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:
    
    def __init__(self, timeToLive: int):
        self.TTL = timeToLive
        self.D = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.D[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.D and self.D[tokenId] + self.TTL > currentTime:
            self.D[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for x in self.D:
            if self.D[x] + self.TTL > currentTime:
                res += 1
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)