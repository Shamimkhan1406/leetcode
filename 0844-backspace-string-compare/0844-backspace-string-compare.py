class Solution(object):
    def backspaceCompare(self, s, t):
        st_s=[]
        for i in s:
            if i == '#':
                if st_s:
                    st_s.pop()
            else:
                st_s.append(i)
        s = ''.join(st_s)
        st_t=[]
        for j in t:
            if j == '#':
                if st_t:
                    st_t.pop()
            else:
                st_t.append(j)
        t = ''.join(st_t)
        
        return s == t

        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        