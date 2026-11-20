class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        max_seen = nums[0]
        right = -1
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            max_seen = max(max_seen,nums[i])
        min_seen = nums[n-1]
        left = n
        for i in range(n-1,-1,-1):
            if nums[i] > min_seen:
                left = i
            min_seen = min(min_seen,nums[i])
        if left == n or right == -1:
            return 0
        return right-left+1

        """
        :type nums: List[int]
        :rtype: int
        """
        