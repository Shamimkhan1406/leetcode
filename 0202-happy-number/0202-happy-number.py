class Solution(object):
    def isHappy(self, n):
        def squre_sum_digit(n):
            sq_s = 0
            while n>0:
                ld = n % 10
                sq_s += ld*ld
                n = n // 10
            return sq_s
        seen = set()
        while n != 1:
            n = squre_sum_digit(n)
            if n in seen:
                return False
            seen.add(n)
        return True

        """
        :type n: int
        :rtype: bool
        """
        