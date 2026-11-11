class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        res = 0
        common = min(need1,need2)
        res += common*min(costBoth,cost1+cost2)
        rem1 = need1-common
        res += rem1 * min(costBoth,cost1)
        rem2 = need2-common
        res += rem2 * min(costBoth,cost2)
        return res
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        