class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0]*n
        p = n-1
        i=0
        j = n-1
        while i<=j:
            if abs(nums[i]) < abs(nums[j]):
                res[p]=nums[j]**2
                j -= 1
            else:
                res[p]=nums[i]**2
                i += 1
            p -= 1
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        