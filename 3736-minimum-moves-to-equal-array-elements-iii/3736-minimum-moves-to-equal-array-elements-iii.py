class Solution(object):
    def minMoves(self, nums):
        m = max(nums)
        c = 0
        for i in nums:
            c += abs(m-i)
        return c
        """
        :type nums: List[int]
        :rtype: int
        """
        