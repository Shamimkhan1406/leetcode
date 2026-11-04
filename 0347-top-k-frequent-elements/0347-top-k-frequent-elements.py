class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        for key,value in freq.items():
            bucket[value].append(key)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        