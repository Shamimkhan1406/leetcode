class Solution(object):
    def totalWaviness(self, num1, num2):
        ans = 0
        for num in range(num1,num2+1):
            s = str(num)
            if len(s) > 2:
                for i in range(1,len(s)-1):
                    if s[i-1]<s[i]>s[i+1] or s[i-1]>s[i]<s[i+1]:
                        ans+=1
        return ans

        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        