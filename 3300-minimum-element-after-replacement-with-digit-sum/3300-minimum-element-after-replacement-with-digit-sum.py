class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            s = 0
            num = nums[i]
            while num > 0:
                s += num % 10
                num //= 10
            nums[i]=s
        return min(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        