class Solution(object):
    def minMoves(self, nums):
        n = len(nums)
        m = max(nums)
        return (n*m)-sum(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        