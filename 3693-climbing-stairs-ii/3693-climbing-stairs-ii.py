class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            # i+1 step
            dp[i]=min(dp[i],dp[i-1]+costs[i-1]+1**2)
            if i >= 2:
                dp[i]= min(dp[i],dp[i-2]+costs[i-1]+2**2)
            if i >= 3:
                dp[i]=min(dp[i],dp[i-3]+costs[i-1]+3**2)
        return dp[n]
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        