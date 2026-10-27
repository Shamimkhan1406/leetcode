class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        res = 0
        n = len(cost)
        for i in range(n):
            if (i+1)%3 != 0:
                res += cost[i]
        return res

        """
        :type cost: List[int]
        :rtype: int
        """
        