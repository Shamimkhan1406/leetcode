from collections import deque
class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        q = deque()
        cost = 0
        ans = 0
        right = n
        for i in range(n-1,-1,-1):
            while q and nums[q[-1]]<nums[i]:
                l = q.pop()
                if q:
                    r = q[-1]
                else:
                    r = right
                cost += (r-l)*(nums[i]-nums[l])
            q.append(i)
            while cost > k:
                j = right-1
                cost -= nums[q[0]]-nums[j]
                if q[0]==j:
                    q.popleft()
                right -= 1
            ans += right-i
        return ans

        

        

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        