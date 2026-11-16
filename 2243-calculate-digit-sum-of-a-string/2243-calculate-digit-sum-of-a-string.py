class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            st = ''
            for i in range(0,len(s),k):
                group = s[i:i+k]
                total = 0
                for ele in group:
                    total += int(ele)
                st += str(total)
            s = st
        return s


        """
        :type s: str
        :type k: int
        :rtype: str
        """
        