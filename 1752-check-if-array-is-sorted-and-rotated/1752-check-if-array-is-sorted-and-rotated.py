class Solution(object):
    def check(self, nums):
        n = len(nums)
        rotate = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                rotate += 1
        return rotate <= 1
        """
        :type nums: List[int]
        :rtype: bool
        """
        