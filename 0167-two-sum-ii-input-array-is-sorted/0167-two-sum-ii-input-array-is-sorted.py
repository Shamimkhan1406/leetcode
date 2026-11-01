class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1,i+1]
            dic[num]=i
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        