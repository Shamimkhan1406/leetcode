class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)
        m = nums[n//2]
        count = 0
        for n in nums:
            count += abs(n-m)
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        