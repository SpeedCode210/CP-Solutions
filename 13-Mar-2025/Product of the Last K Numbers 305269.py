# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

from collections import deque 

class ProductOfNumbers:

    def __init__(self):
        self._l = [0]
        self._z = [0]

    def add(self, num: int) -> None:
        if num == 0:
            self._l.append(0)
            self._z.append(len(self._z))
        elif self._l[-1] == 0:
            self._l.append(num)
            self._z.append(self._z[-1])
        else:
            self._l.append(num*self._l[-1])
            self._z.append(self._z[-1])

    def getProduct(self, k: int) -> int:
        if len(self._z) - self._z[-1] <= k:
            return 0
        else:
            return self._l[-1]//(self._l[-k-1] if self._l[-k-1] != 0 else 1)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)