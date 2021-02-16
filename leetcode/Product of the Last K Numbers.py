class ProductOfNumbers:
    
    def __init__(self):
         self.prodList = [1]

    def add(self, num: int) -> None:
        if num > 0:
            self.prodList.append(num * self.prodList[-1])
        else:
            self.prodList.clear()
            self.prodList.append(1)

    def getProduct(self, k: int) -> int:
        if k > len(self.prodList) - 1:
            return 0
        else:
            return self.prodList[-1] // self.prodList[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)