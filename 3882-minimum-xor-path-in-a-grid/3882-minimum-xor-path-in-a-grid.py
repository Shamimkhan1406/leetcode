class Solution(object):
    def minCost(self, grid):
        r = len(grid)
        c = len(grid[0])
        dp = [[set() for _ in range(c)] for _ in range(r)]
        dp[0][0].add(grid[0][0])
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    continue
                if i > 0:
                    for k in dp[i-1][j]:
                        dp[i][j].add(k^grid[i][j])
                if j > 0:
                    for k in dp[i][j-1]:
                        dp[i][j].add(k^grid[i][j])
        return min(dp[r-1][c-1])
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        