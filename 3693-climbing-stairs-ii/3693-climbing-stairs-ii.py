class Solution(object):
    def climbStairs(self, n, costs):
        memo = [-1]*(n+1)
        def dfs(i):
            if i == n:
                return 0
            if memo[i]!= -1:
                return memo[i]
            ans = float('inf')
            for jump in range(1,4):
                j = jump+i
                if j <= n:
                    jump_cost = costs[j-1]+jump**2
                    ans = min(ans,jump_cost+dfs(j))
            memo[i] = ans
            return memo[i]
        return dfs(0)
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        