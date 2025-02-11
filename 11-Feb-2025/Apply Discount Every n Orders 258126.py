# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.counter = 0
        self.stock = {products[i]: prices[i] for i in range(len(prices))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.counter += 1
        total = sum([amount[i]*self.stock[product[i]] for i in range(len(amount))])
        if self.counter % self.n == 0:
            total = total *((100-self.discount)/100)
        return total
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)