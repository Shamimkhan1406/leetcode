class Solution(object):
    def minOperations(self, s):
        if ''.join(sorted(s)) == s:
            return 0
        if len(s)==2:
            return -1
        sm = min(s)
        mx = max(s)
        if s[0] == sm or s[-1] == mx:
            return 1
        for c in s[1:-1]:
            if c == sm or c == mx:
                return 2
        return 3
        """
        :type s: str
        :rtype: int
        """
        