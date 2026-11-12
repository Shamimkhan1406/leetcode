class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = 1
        dec = 1
        li = 0
        ld = 0
        for r in range(1,len(nums)):
            if nums[r]>nums[r-1]:
                inc = max(inc,r-li+1)
            else:
                li = r
            if nums[r]<nums[r-1]:
                dec = max(dec,r-ld+1)
            else:
                ld = r
        return max(inc,dec)

        """
        :type nums: List[int]
        :rtype: int
        """
        