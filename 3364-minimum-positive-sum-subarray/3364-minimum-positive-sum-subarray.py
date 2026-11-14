class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        prefix = [0]*(n+1)
        ans = float('inf')
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        for length in range(l,r+1):
            for i in range(n-length+1):
                j = i+length
                s = prefix[j]-prefix[i]
                if s > 0:
                    ans = min(ans,s)
        return ans if ans != float('inf') else -1

        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        