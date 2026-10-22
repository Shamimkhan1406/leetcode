class Solution(object):
    def minElement(self, nums):
        res = []
        for num in nums:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            res.append(s)
        return min(res)
        """
        :type nums: List[int]
        :rtype: int
        """
        