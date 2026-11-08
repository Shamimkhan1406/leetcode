class Solution(object):
    def countServers(self, grid):
        n=len(grid)
        m=len(grid[0])
        r_c = [0]*n
        c_c = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    r_c[i]+=1
                    c_c[j]+=1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if r_c[i]>1 or c_c[j]>1:
                        res += 1
        return res
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        