class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1]*num)
        """
        :type num: int
        :rtype: None
        """
        

    def getProduct(self, k):
        if k >= len(self.prefix):
            return 0
        else:
            return self.prefix[-1]//self.prefix[-k-1]
        """
        :type k: int
        :rtype: int
        """
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)