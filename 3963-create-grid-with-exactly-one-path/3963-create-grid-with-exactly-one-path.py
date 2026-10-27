class Solution(object):
    def createGrid(self, m, n):
        res = [['#']*n for _ in range(m)]
        for i in range(n):
            res[0][i]='.'
        for j in range(m):
            res[j][n-1]='.'
        return [''.join(row) for row in res]
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        