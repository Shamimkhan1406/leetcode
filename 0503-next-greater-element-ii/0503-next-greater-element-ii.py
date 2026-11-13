class Solution(object):
    def nextGreaterElements(self, nums):
        st = []
        n = len(nums)
        res = [-1]*n
        for _ in range(2):
            for i in range(n):
                while st and nums[st[-1]]<nums[i]:
                    res[st.pop()]=nums[i]
                st.append(i)
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        